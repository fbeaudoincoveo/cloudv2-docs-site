import gitHelper
import httpHelper
import fileHelper
import json
import re
import directoryHelper
from datetime import datetime


CONFIG_FILE = "./diff_script_config.yml"

configData = fileHelper.load_yaml_config_file(CONFIG_FILE)
DEBUG = configData["debug"]


class Repository:
    def __init__(self):
        self.accessToken = configData["repository"]["accessToken"]
        self.tempOutputJsonPath = configData["repository"]["tempOutputJsonPath"]
        self.outputYamlPath = configData["repository"]["outputYamlPath"]
        self.mdPagesPath = configData["repository"]["mdPagesPath"]
        self.mdLayout = configData["repository"]["mdLayout"]
        self.upstreamBranch = configData["repository"]["upstreamBranch"]
        self.baseBranch = configData["repository"]["baseBranch"]
        self.baseCommitMessage = configData["repository"]["baseCommitMessage"]
        self.pullRequestMessage = configData["repository"]["pullRequestMessage"]


class Platform:
    def __init__(self):
        self.environment = configData["platform"]["environment"]
        self.apiList = configData["platform"]["apiList"]
        self.methodList = configData["platform"]["methodList"]
        self.host1 = configData["platform"]["host1"]
        self.host2 = configData["platform"]["host2"]
        self.apiDocsPath = configData["platform"]["apiDocsPath"]

    def get_host(self):
        return self.host1 + self.environment + self.host2


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

repository = Repository()
platform = Platform()

gitHelper.checkout(repository.upstreamBranch, DEBUG)
if not fileHelper.file_exists(repository.mdPagesPath):
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
                 api + "\n---"
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
