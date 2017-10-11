class Repository:
    def __init__(self, config_data):
        self.accessToken = config_data["repository"]["accessToken"]
        self.tempOutputJsonPath = config_data["repository"]["tempOutputJsonPath"]
        self.outputYamlPath = config_data["repository"]["outputYamlPath"]
        self.mdPagesPath = config_data["repository"]["mdPagesPath"]
        self.mdLayout = config_data["repository"]["mdLayout"]
        self.upstreamBranch = config_data["repository"]["upstreamBranch"]
        self.baseBranch = config_data["repository"]["baseBranch"]
        self.baseUpstreamCommitMessage = config_data["repository"]["baseUpstreamCommitMessage"]
        self.baseDeployCommitMessage = config_data["repository"]["baseDeployCommitMessage"]
        self.upstreamPullRequestMessage = config_data["repository"]["upstreamPullRequestMessage"]


class Platform:
    def __init__(self, config_data):
        self.environment = config_data["platform"]["environment"]
        self.apiList = config_data["platform"]["apiList"]
        self.methodList = config_data["platform"]["methodList"]
        self.host1 = config_data["platform"]["host1"]
        self.host2 = config_data["platform"]["host2"]
        self.apiDocsPath = config_data["platform"]["apiDocsPath"]

    def get_host(self):
        return self.host1 + self.environment + self.host2