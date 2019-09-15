from flask import Flask
from settings import Settings


app = Flask(__name__)
app.config.from_object(Settings)

'''
App Blueprint registration
'''
from src._blueprints import prediction_bp
from src._blueprints import status_bp

app.register_blueprint(prediction_bp)
app.register_blueprint(status_bp)
