from flask import Blueprint
from flask_restful import Api

# Api prefix
apiPrefix = '/api/v1'

'''
BluePrint Creation
Use BluePrints to create Url Prefixes
'''
prediction_bp = Blueprint('prediction', __name__, url_prefix=apiPrefix + '/prediction')
status_bp = Blueprint('status', __name__, url_prefix=apiPrefix + '/status')

'''
Must create a new api with the new blueprint
'''
api_prediction = Api(prediction_bp)
api_status = Api(status_bp)

'''
Load Routes
'''
from src import routes