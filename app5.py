
from flask import Flask, request, render_template
from joblib import load
app = Flask(__name__)
model= load('r1.save')
trans=load('s1')

@app.route('/')
def home():
    return render_template('h1.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[x for x in request.form.values()]]
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    
    
    return render_template('h1.html', prediction_text='Price {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
