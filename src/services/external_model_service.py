import json
import requests


class ExternalPredictService:

    def __init__(self, url):
        self.__url = url

    def get_prediction(self, features):
        """
        This is for querying an external model (for example a tensorflow serve API) to get the prediction.
        The RestAPI is not the best option for the sakes of speed, the best option is GRPC but, since installing GRPC
        is a long process and this is meant to be easily tested, here I used the Rest API.
        :param features: The NNET input.
        :return: The prediction.
        """
        data = json.dumps({"signature_name": "serving_default", "inputs": {"features": features.tolist()}})

        headers = {"content-type": "application/json"}
        json_response = requests.post(self.__url,
                                      data=data,
                                      headers=headers)
        prediction = json.loads(json_response.text)['outputs'][0][0]
        return prediction
