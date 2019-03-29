from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# D,Name,Address,Tshirt,Shirt,Jeans,Trousers,Curtain,Towel,Blanket,Bedsheet

class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    tshirt = StringField('tshirt', validators=[DataRequired()])
    shirt = StringField('shirt', validators=[DataRequired()])
    jeans = StringField('jeans', validators=[DataRequired()])
    trousers = StringField('trousers', validators=[DataRequired()])
    curtain = StringField('curtain', validators=[DataRequired()])
    towel = StringField('towel', validators=[DataRequired()])
    blanket = StringField('blanket', validators=[DataRequired()])
    bedsheet = StringField('bedsheet', validators=[DataRequired()])

    submit = SubmitField('Submit')

