from subprocess import call
from httpHelper import basic_post


def checkout(branch, debug=False):
    if debug:
        print "Checking out branch %s" % branch
    call("git checkout %s" % branch, shell=True)


def add(file_to_add, debug=False):
    if debug:
        print "Adding %s." % file_to_add
    call("git add %s" % file_to_add, shell=True)


def commit_all(commit_message, debug=False):
    if debug:
        print "Committing all changes."
    call("git commit -a --message=%s" % commit_message, shell=True)


def push(debug=False):
    if debug:
        print "Pushing."
    call("git push", shell=True)


def create_pull_request(access_token, title, head, base, debug=False):
    uri = "https://api.github.com/repos/coveo/cloudv2-docs-site/pulls"
    headers = {'Authorization': 'token %s' % access_token}
    body = {'title': title, 'head': head, 'base': base}
    pull_request = basic_post(uri, headers, body, debug)
    if debug:
        print "Access token: %s" % access_token
        print "Title: %s" % title
        print "Head: %s" % head
        print "Base: %s" % base
        print "Status code: %s" % pull_request.status_code
        print pull_request.content
