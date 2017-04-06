from subprocess import call
import os


def make_directory(directory_to_create, debug=False):
    if debug:
        print "Creating directory: %s." % directory_to_create
    os.makedirs(directory_to_create)


def recursively_delete_directory(directory_to_delete, debug=False):
    if debug:
        print "Deleting directory: %s" % directory_to_delete
    call("rm -R %s" % directory_to_delete, shell=True)