# heavywater-document-classification
## 1 Model development 
The support vector machine model is trained on the dataset. Check training_model.ipynb
## 2 Test Webservice
The Model is deployed as a flask web application using AWS elastic beanstalk. 
####(1) Upload csv file to website
Go to http://documentclassification-env-1.eba-u5nvpkwp.us-east-1.elasticbeanstalk.com and upload an csv file. The csv file should be smaller than 60M. The csv file should not include any headers and NAN values. 
####(2) Send a json format request to the API
Send a json data {'words':"xxxxx document words xxxxx"} to http://documentclassification-env-1.eba-u5nvpkwp.us-east-1.elasticbeanstalk.com/predict The API is going to send back the prediction and a confidence score as following: {'confidence': 'xx%', 'prediction': 'xxxx'}
