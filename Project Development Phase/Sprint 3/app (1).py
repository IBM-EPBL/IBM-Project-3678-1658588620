import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__) # initializing the flask app
model = pickle.load(open('CKD.pkl','rb')) # load the model

@app.route('/') # route to display the home page
def home():
     return render_template('home.html') # rendering the home page
@app.route('/Prediction',methods=['POST','GET'])
def Prediction(): #route to display prediction page
    return render_template('indexnew.html')
@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('home.html')

@app.route('/predict',methods=['POST']) # route to show the prediction in a web UI
def predict():
    # reading the input given by the user
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ['blood_urea','blood glucose random','coronary_artery_disease',
    'anemia','pus_cell','red_blood_cells','diabetesmellitus','pedal_edema']

    df = pd.DataFrame(features_value, columns=features_name)

    output = model.predict(df) # predictions using the loaded model file

    # showing the prediction results in a UI # showing the prediction results in a UI
    return render_template('result.html',prediction_text=output)

if __name__ == '__main__':
    app.run(debug=True) # running the app
