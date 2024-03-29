import boto3


class S3Service:

    def __init__(self, bucket_name, access_key=None, secret_key=None):
        self.bucket_name = self.__generate_bucket_name()
        if access_key is not None:
            self.__client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        else:
            self.__client = boto3.client('s3')

    def __generate_bucket_names(self) -> str:
        # Just in case you need some expression to build the buckets name.
        return self.bucket_name

    def download_file(self, local_file_path):
        try:
            self.__client.download_file(self.bucket_name,
                                        self.__remote_file_path(
                                            local_file_path),
                                        local_file_path)
        except Exception as e:
            raise e

    def get_bucket_content(self):
        return self.__client.list_objects(Bucket=self.bucket_name)['Contents']

    @staticmethod
    def __remote_file_path(file_path):
        file_name = file_path.split('/')[-1]
        return file_name
