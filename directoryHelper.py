from subprocess import call


def make_directory(directory_to_create, debug=False):
    if debug:
        print "Creating directory: %s." % directory_to_create
    call("mkdir %s" % directory_to_create, shell=True)


def recursively_delete_directory(directory_to_delete, debug=False):
    if debug:
        print "Deleting directory: %s" % directory_to_delete
    call("rm -R %s" % directory_to_delete, shell=True)