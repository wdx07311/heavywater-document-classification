# Heavywater-document-classification
## 1 Model development 
The support vector machine model is trained on the dataset. Check training_model.ipynb
## 2 Test Webservice
The Model is deployed as a flask web application using AWS Elastic Beanstalk. 
#### (1) Upload csv file to website
Go to http://documentclassification-env-1.eba-u5nvpkwp.us-east-1.elasticbeanstalk.com and upload an csv file which contains multiple document text. The csv file should be smaller than 60M. The csv file should not include any headers and NAN values. Check some test cases in test_cases file. The website is going to return a csv file with predicted classes for test data. 
#### (2) Send a json format data to the API
This is used to predict a single document. Send a json format data `{'words':"xxxxx document words xxxxx"}` to http://documentclassification-env-1.eba-u5nvpkwp.us-east-1.elasticbeanstalk.com/predict . The API is going to send back the prediction and a confidence score as following: `{'confidence': 'xx%', 'prediction': 'xxxx'}`. <br/>
Here are some sample codes in python to test API:<br/>
`import request`
`words = {'words':'XXXXX XXXXX XXXXX'}`
url = 'http://documentclassification-env-1.eba-u5nvpkwp.us-east-1.elasticbeanstalk.com/predict'


r = requests.post(url_2,json=words)


print(r.json())`

