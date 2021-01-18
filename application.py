
# importing Flask and other modules 
from flask import Flask, request, render_template, make_response, jsonify, send_file
import numpy as np
import pandas as pd
from joblib import dump, load

model =  load('model_whole_dataset_svc_linear_C_1.joblib')

def predict_text(test_data):

   predictions = model.predict(test_data)
   predictions = pd.DataFrame(predictions)# transform numpy array to pandas dataframe

   return predictions

# Flask constructor 
application = Flask(__name__)    

@application.route('/', methods =["GET", "POST","PUT"]) 
def text_classify(): 

   if request.method == "POST":
      got_json = request.files['test_file']
      test_df = pd.read_csv(got_json,header = None)#Assuming the uploaded csv file doesn't include headers
      test_df = test_df[test_df.columns[-1]]#Get the last column of csv file, sometimes the first column is index
      predictions = predict_text(test_df)#predict to get result
      response = make_response(predictions.to_csv(index = False, header = False))
      response.headers["Document"] = "attachment; filename=predictions.csv"
      response.headers["Content-Type"] = "text/csv"
      return response

   return render_template("index.html") 

@application.route('/predict', methods =["GET", "POST","PUT"]) 
def predict():
   words = request.get_json()
   words = [words['words']]
   prediction = model.predict_proba(words)
   result = {'prediction':model.classes_[np.argmax(prediction)],'confidence':str(int(np.max(prediction)*100))+'%'}
   return jsonify(result)

  
if __name__=='__main__': 
   application.run(debug = True) 
