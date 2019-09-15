from jsonschema import validate as json_validate
import simplejson as json
from src.exceptions.input_validator import InputValidatorBadRequest, InputValidatorEmptyJson
from jsonschema.exceptions import ValidationError
from os.path import dirname


class Validator:

    def __init__(self):
        self.__schemas = {}
        self.__schemas_path = dirname(__file__) + "/schemas_json/"

    def validate(self, request, attr_name):
        json_input = request.get_json(force=True, silent=True)
        # if json_input is None:
        #     return None
        if not json_input:
            raise InputValidatorEmptyJson
        try:
            json_validate(json_input, self.__get_schema(attr_name))
        except ValidationError as e:
            raise InputValidatorBadRequest(e)
        data = json_input[attr_name] if attr_name in json_input else None

        return data

    def __get_schema(self, name):
        if name not in self.__schemas.keys():
            self.__schemas[name] = self.__load_schema_file(name)
        return self.__schemas[name]

    def __load_schema_file(self, name):
        file_name = "{0}{1}.json".format(self.__schemas_path, name)
        with open(file_name, 'r') as f:
            schema_data = f.read()
        return json.loads(schema_data)
