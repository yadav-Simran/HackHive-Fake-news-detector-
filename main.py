import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
application = Flask(__name__) #Initialize the flask App
model = pickle.load(open('HackHive_Pkl', 'rb'))

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('Kavach_2023/index.html', prediction_text='Fake News Detection - Enter News $ {}'.format(output))

if __name__ == "__main__":
    application.run(debug=True)