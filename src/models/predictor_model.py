import pickle
import os


class PredictionModel:

    def __init__(self, model_path: str, external_service, s3_service):
        self.__s3_service = s3_service
        self.__model, self.__transformation = self.__load_model_from_file(model_path)
        self.__external_service = external_service

    def __load_model_from_file(self, model_path):
        """This method loads the .mdl file configured on the Settings.
        To load a model that works, the parts have to be:
         - A "model" that have at least one method "predict" that takes a np.array with shape (1, M)
         as argument and returns a list (or array) of predictions.
         - A "transformation" that have at least one method "transform" that takes  a np.array with dimensions
         (1, N) as argument and returns a np.array of shape (1, M).
        """
        if not os.path.isfile(model_path):
            self.__s3_service.download_file(model_path)

        with open(model_path, 'rb') as f:
            [model, transformation] = pickle.load(f)

        return model, transformation

    def __transform_data(self, features):
        """This method conforms the data transformation pipeline.
        The transformation takes places in two steps: fist masking the columns and then transforming the data.
        """
        transformed_features = self.__transformation.transform(features)
        return transformed_features

    def __model_predict(self, transformed_features):
        """Prediction pipeline of the model."""
        if self.__model is None:  # To use the external service load a model file with "None" model.
            prediction = self.__external_service.get_prediction(transformed_features)
        else:
            prediction = self.__model.predict(transformed_features)[0]
        return prediction


    def predict(self, features):
        """This method is in charge of executing the whole pipeline for an input to the output."""
        transformed_features = self.__transform_data(features)
        prediction = self.__model_predict(transformed_features)
        return prediction
