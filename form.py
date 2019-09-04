from flask_wtf import FlaskForm
from wtforms import IntegerField,DecimalField, SubmitField
from wtforms.validators import DataRequired

class Prediction (FlaskForm):
    bedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired()])
    bathrooms  = IntegerField('Number of Bathrooms', validators=[DataRequired()])
    sqft_living = DecimalField('sqft living', validators=[DataRequired()])
    sqft_lot = DecimalField('sqft lot', validators=[DataRequired()])
    floors = IntegerField('floors', validators=[DataRequired()])
    sqft_lot15 = DecimalField('sqft lot15', validators=[DataRequired()])
    sqft_above = DecimalField('sqft above', validators=[DataRequired()])<br /><br />

        {{ myform.sqft_lot15.label() }}
        {{ myform.sqft_lot15() }}

    yr_built = IntegerField('Year built', validators=[DataRequired()])
    condition  = IntegerField('condition', validators=[DataRequired()])
    zipcode = IntegerField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Predict')