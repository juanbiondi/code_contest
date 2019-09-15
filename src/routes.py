from src import app
# Exceptions
# BluePrints Imports
from src._blueprints import api_prediction
from src._blueprints import api_status
# controllers Imports
from src.controllers import prediction_controllers
from src.controllers import status_controllers

'''
Routes Urls
'''
api_prediction.add_resource(prediction_controllers.PredictionController,
                            '/predict',
                            endpoint="predict")

api_status.add_resource(status_controllers.Ping,
                        '/ping',
                        endpoint="ping")


@app.errorhandler(404)
def not_found(e):
    return 'Not Found', 404
