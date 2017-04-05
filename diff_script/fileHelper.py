from subprocess import call
import os.path
import yaml


def create_file_from_data(data, file_to_create, debug=False):
    if debug:
        print "Creating file: %s" % file_to_create
    new_file = open(file_to_create, "w")
    new_file.write(data)
    new_file.close()


def create_yaml_file_from_json_file(input_json_file, output_yaml_file, debug=False):
    if debug:
        print "Creating YAML file %s from JSON file %s" % (output_yaml_file, input_json_file)
    call("json2yaml %s > %s" % (input_json_file, output_yaml_file), shell=True)


def file_exists(file_to_find, debug=False):
    if debug:
        print "Trying to locate %s" % file_to_find
    return os.path.exists(file_to_find)


def load_yaml_config_file(file_to_load):
    stream = open(file_to_load, "r")
    config_data = yaml.load(stream)
    stream.close()
    return config_data
