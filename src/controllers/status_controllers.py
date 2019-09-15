from flask_restful import Resource
import time


class Ping(Resource):

    @staticmethod
    def get():
        """
        This method is used to check if the process is behaving properly.
        :return: Json with status and timestamp
        """
        return {'status': 'ok', 'timestamp': round(time.time() * 1000)}
