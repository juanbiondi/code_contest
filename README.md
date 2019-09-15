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
 
To run the API you have just to run the flask bu simply sunning the "main.py" file or, for production environments with "gunicorn":
 - ```gunicorn -b localhost:8880 --workers=3 --worker-class=gevent --worker-connections=10000 main:app```
 
The API itself will download a sample model.

-----------------

On production, to retrain the models, the best way is to, run all the Notebooks again and make sure that the model is working properly.

Doing that, is just matter to upload the new model to S3 and, reconfigure the .env and rerun the API.   
