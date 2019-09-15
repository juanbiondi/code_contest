from src.models import ModelContainer

import numpy as np


class PredictService:

    def __init__(self):
        pass

    @staticmethod
    def get_prediction(features):
        # Cast and prepare the input
        features = np.array(features, dtype=np.float32).reshape(1, -1)

        model = ModelContainer.predictionModel()
        prediction = model.predict(features)
        return prediction
