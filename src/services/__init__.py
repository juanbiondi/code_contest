'''
    Services Registration
'''
# Imports dependency injector
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from src.services.predict_service import PredictService

from settings import Settings


class ServiceContainer(containers.DeclarativeContainer):
    ''' Register Services '''

    predictService = providers.Singleton(PredictService)
