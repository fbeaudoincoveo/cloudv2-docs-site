from os import makedirs
from os import rmdir


def make_directory(directory_to_create, debug=False):
    if debug:
        print "Creating directory: %s ..." % directory_to_create
    makedirs(directory_to_create)


def delete_directory(directory_to_delete, debug=False):
    if debug:
        print "Deleting directory: %s ..." % directory_to_delete
    rmdir(directory_to_delete)