from subprocess import call


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
