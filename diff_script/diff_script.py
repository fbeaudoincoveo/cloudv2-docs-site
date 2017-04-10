import gitHelper
import httpHelper
import fileHelper
import json
import re
import directoryHelper
from datetime import datetime
import config_classes


CONFIG_FILE = "./diff_script_config.yml"

configData = fileHelper.load_yaml_config_file(CONFIG_FILE)
DEBUG = configData["debug"]

# This removes the "_1" that sometimes appear at the end of operationIds in the Swagger JSON as a result of the multiple
# proxy instances.
def clean_json_data(data):
    for path in data["paths"]:
        for method in platform.methodList:
            if method in data["paths"][path] and "operationId" in data["paths"][path][method]:
                matchObject = re.match(r'\w+(_\d+)+', data["paths"][path][method]["operationId"])
                if matchObject:
                    data["paths"][path][method]["operationId"] = \
                        data["paths"][path][method]["operationId"].replace(matchObject.group(1), "")
    data = json.dumps(data)
    return data

repository = config_classes.Repository(configData)
platform = config_classes.Platform(configData)

gitHelper.checkout(repository.upstreamBranch, DEBUG)
if not fileHelper.file_exists(repository.tempOutputJsonPath):
    directoryHelper.make_directory(repository.tempOutputJsonPath, DEBUG)

for api in platform.apiList:

    swaggerSpecificationPath = platform.get_host() + platform.apiDocsPath + api

    request = httpHelper.basic_get(swaggerSpecificationPath, DEBUG)

    if request.status_code == 200:

        cleanData = clean_json_data(json.loads(request.content))

        jsonTempFile = repository.tempOutputJsonPath + api + ".json"
        fileHelper.create_file_from_data(cleanData, jsonTempFile, DEBUG)

        yamlFile = repository.outputYamlPath + api + ".yml"
        fileHelper.create_yaml_file_from_json_file(jsonTempFile, yamlFile, DEBUG)

        gitHelper.add(yamlFile, DEBUG)

        markdownFile = repository.mdPagesPath + api + ".md"
        if not fileHelper.file_exists(repository.mdPagesPath):
            directoryHelper.make_directory(repository.mdPagesPath)
        mdData = "---\nlayout: " + repository.mdLayout + "\ntitle: \'" + api + \
                 "\'\ncategories: api_docs\nswagger: " + yamlFile + "\npermalink: " + repository.mdPagesPath + \
                 api + "\nghPagesSiteName: " + repository.ghPagesSiteName + "\n---"
        fileHelper.create_file_from_data(mdData, markdownFile, DEBUG)

        gitHelper.add(markdownFile, DEBUG)

    else:
        print "Could not get Swagger specification from " + swaggerSpecificationPath + " ."

directoryHelper.recursively_delete_directory(repository.tempOutputJsonPath, DEBUG)

commitMessage = repository.baseCommitMessage + str(datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
gitHelper.commit_all(commitMessage, DEBUG)

gitHelper.push(DEBUG)
gitHelper.create_pull_request(repository.accessToken, repository.pullRequestMessage,
                              repository.upstreamBranch, repository.baseBranch, DEBUG)
