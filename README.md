# Heavywater-document-classification
## 1 Model development (Check training_model.ipynb)
(1) Data exploration and use TF-IDF method to vectorize the data<br/>
(2) A support vector machine model with linear kernel is trained on the dataset.<br/>
(3) Grid search is used to find the best parameters C for support vector machine.<br/>
(4) The accuracy of the model is around 87%.<br/>
(5) The full dataset is used to train the model for deployment.<br/>
## 2 Test Webservice
The Model is deployed as a flask web application using AWS Elastic Beanstalk. 
#### (1) Upload csv file to website
Go to http://documentclassification-env-1.eba-u5nvpkwp.us-east-1.elasticbeanstalk.com and upload an csv file which contains multiple document text. <br/>
The csv file should be smaller than 60M. The csv file should not include any headers and NAN values. Check some test cases in test_cases file. <br/>
The website is going to return a csv file with predicted classes for test data. <br/>
Large file cause longer time for the website to response. <br/>
#### (2) Send a json format data to the API
Each call is used to predict a single document. Send a json format data `{'words':"xxxxx document words xxxxx"}` to http://documentclassification-env-1.eba-u5nvpkwp.us-east-1.elasticbeanstalk.com/predict . The API is going to send back the prediction and a confidence score as following: `{'confidence': 'xx%', 'prediction': 'xxxx'}`. <br/>
Here are some sample codes in python to test API:<br/>
`import request`<br/>
`words = {'words':'XXXXX XXXXX XXXXX'}`<br/>
`url = 'http://documentclassification-env-1.eba-u5nvpkwp.us-east-1.elasticbeanstalk.com/predict'`<br/>
`r = requests.post(url,json=words)`<br/>
`print(r.json())`<br/>

