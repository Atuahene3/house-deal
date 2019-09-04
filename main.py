from flask import Flask,render_template,redirect,flash,url_for
from form import Prediction 
from joblib import load
app = Flask(__name__)

app.config['SECRET_KEY'] = 'bb82e940866b9446a62342d10665020f'
@app.route('/' , methods=['GET','POST'])
def home():
    form = Prediction()
    result = ''
    if form.validate_on_submit():
        data = [form.bedrooms.data,form.bathrooms.data, form.sqft_living.data,form.sqft_lot.data, form.floors.data,
                form.sqft_lot15.data, form.sqft_above.data, form.yr_built.data, form.condition.data, form.zipcode.data]

        model = load('model.joblib')

        result = model.predict([data])
        result = str(result).strip('[]')
        flash('the price is $' + result)
        return redirect(url_for('home'))
    return render_template('home.html',myform=form)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)
