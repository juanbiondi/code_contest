from flask_restful import Resource, request, marshal_with
from src.input_validator import validator

from src.decorators.prediction import prediction_fields

from src.services import ServiceContainer


class PredictionController(Resource):

    @marshal_with(prediction_fields)
    def post(self):
        """
        This controller validates the input features to be an array of 47 number elements.
        :return: Prediction of the model.
        """
        features = validator.validate(request, 'features')

        predict_service = ServiceContainer.predictService()

        prediction = predict_service.get_prediction(features)
        return {'prediction': prediction}
