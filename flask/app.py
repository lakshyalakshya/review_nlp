from flask import Flask, render_template, request
import pickle
import sklearn
app = Flask(__name__)


import pickle

# read python dict back from the file
file = open(r'F2_model.pkl', 'rb')
model = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        my_prediction = model.predict(data)
        return render_template('result.html', prediction=my_prediction)


if __name__== "__main__":
    print("hello")
    app.run(debug=True)