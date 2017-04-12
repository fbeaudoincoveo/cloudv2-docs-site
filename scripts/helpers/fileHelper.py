from subprocess import call
from os import path
from os import remove
import yaml


def create_file_from_data(data, file_to_create, debug=False):
    if debug:
        print "Creating file: %s ..." % file_to_create
    new_file = open(file_to_create, "w")
    new_file.write(data)
    new_file.close()


def create_yaml_file_from_json_file(input_json_file, output_yaml_file, debug=False):
    if debug:
        print "Creating YAML file %s from JSON file %s ..." % (output_yaml_file, input_json_file)
    call("json2yaml %s > %s" % (input_json_file, output_yaml_file), shell=True)


def file_exists(file_to_find, debug=False):
    file_exists = path.exists(file_to_find)
    if debug:
        status = " found." if file_exists else " not found."
        print file_to_find + status
    return file_exists


def load_yaml_file(file_to_load, debug=False):
    if debug:
        print "Loading %s" % file_to_load
    stream = open(file_to_load, "r")
    data = yaml.load(stream)
    stream.close()
    return data


def delete_file(file_to_delete, debug=False):
    if debug:
        print "Deleting %s" % file_to_delete
    remove(file_to_delete)


def load_yaml_config_file():
    return load_yaml_file("../config.yml")
