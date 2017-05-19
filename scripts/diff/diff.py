import sys
sys.path.append('../helpers')
import directoryHelper
import fileHelper
import gitHelper
import httpHelper
import config_classes
import json
import re
from datetime import datetime


configData = fileHelper.load_yaml_config_file()
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

for requiredPath in [repository.tempOutputJsonPath, repository.outputYamlPath]:
    if not fileHelper.file_exists(requiredPath, DEBUG):
        directoryHelper.make_directory(requiredPath, DEBUG)

for api in platform.apiList:

    swaggerSpecificationPath = platform.get_host() + platform.apiDocsPath + api + "?group=public"

    request = httpHelper.basic_get(swaggerSpecificationPath, DEBUG)

    if request.status_code == 200:

        cleanData = clean_json_data(json.loads(request.content))

        jsonTempFile = repository.tempOutputJsonPath + api + ".json"
        fileHelper.create_file_from_data(cleanData, jsonTempFile, DEBUG)

        yamlFile = repository.outputYamlPath + api + ".yml"
        fileHelper.create_yaml_file_from_json_file(jsonTempFile, yamlFile, DEBUG)

        gitHelper.add(yamlFile, DEBUG)

        fileHelper.delete_file(jsonTempFile, DEBUG)

    else:
        print "Could not get Swagger specification from " + swaggerSpecificationPath + " ."

directoryHelper.delete_directory(repository.tempOutputJsonPath, DEBUG)

commitMessage = repository.baseUpstreamCommitMessage + str(datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
gitHelper.commit_all(commitMessage, DEBUG)

gitHelper.push(DEBUG)
gitHelper.create_pull_request(repository.accessToken, repository.upstreamPullRequestMessage,
                              repository.upstreamBranch, repository.baseBranch, DEBUG)
