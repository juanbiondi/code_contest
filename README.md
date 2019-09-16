# Code contest

This repo is for the code contest and contains the API for serving the trained model on the notebooks.

This api is entirely built in Python 3.

To run this API you have to install Python 3 and "virtualenv": 
 - ```sudo apt-get install python3-pip```
 - ```sudo pip3 install virtualenv ```
 - ```virtualenv -p python3 venv```
 
Then you have to activate the venv and install the "requirements":
 - ```source venv/bin/activate```
 - ```pip install -r requirements.txt```
 
Then you have to proper configure the ".env".
 
To run the API you have just to run the flask bi simply running the "main.py" file or, for production environments with "gunicorn":
 - ```gunicorn -b localhost:8880 --workers=3 --worker-class=gevent --worker-connections=10000 main:app```
 
Other form to run this API for production environments is to compile and run the included "Dockerfile" that is configured to run the application with proper configurations.
This is useful if you are using (for example) EBS from AWS or simply have a cluster with docker instances running.  
Note that you have to run the docker instance exporting the AWS credentials like:

```
AWS_ACCESS_KEY_ID=$(aws --profile default configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY=$(aws --profile default configure get aws_secret_access_key)

docker build -t my_app .
docker run -it --rm \
   -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
   -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
```

With AWS credentials configured the API itself will download a sample model.
If you dont have configured the keys, just download the model (and configure the .env).  

-----------------

On production, to retrain the models, the best way is to, run all the Notebooks again and make sure that the model is working properly.

Doing that, is just matter to upload the new model to S3 and, reconfigure the ".env" and rerun the API.
