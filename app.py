from flask import Flask, render_template, request
import pickle

model = pickle.load(open('savedmodel.sav', 'rb'))

app = Flask(__name__)


@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    age = float(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    cyclelength = float(request.form['cyclelength'])
    weightgain = float(request.form['weightgain'])
    hairloss = float(request.form['hairloss'])
    pimples = float(request.form['pimples'])
    exercise = float(request.form['exercise'])
    fastfood = float(request.form['fastfood'])
    hairgrowth = float(request.form['hairgrowth'])
    skindark = float(request.form['skindark'])
    waist = float(request.form['waist'])
    hip = float(request.form['hip'])
    bmi = float(request.form['bmi'])
    pred = model.predict([[age, weight, height, cyclelength, weightgain, hairloss, 
                             pimples, exercise, fastfood,
                             hairgrowth, skindark, waist, hip, bmi]])[0]
    return render_template('after.html', data = pred)


if __name__ == "__main__":
    app.run(debug=True)
