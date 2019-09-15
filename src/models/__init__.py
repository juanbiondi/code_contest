# Imports dependency injector
import dependency_injector.containers as containers
import dependency_injector.providers as providers

# Imports Service Classes
from settings import Settings
#
from src.models.predictor_model import PredictionModel
from src.services.external_model_service import ExternalPredictService


class ModelContainer(containers.DeclarativeContainer):

    externalModelService = providers.Singleton(ExternalPredictService,
                                               url=Settings.MODEL_URL)
    predictionModel = providers.Singleton(PredictionModel,
                                          model_path=Settings.MODEL_PATH,
                                          external_service=externalModelService)
