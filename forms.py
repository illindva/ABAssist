from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, FieldList, FormField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                         validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                   validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered. Please use a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# Example form for external system connection testing
class ConnectionTestForm(FlaskForm):
    connection_type = SelectField('Connection Type', 
                              choices=[('oracle', 'Oracle Database'), 
                                       ('sybase', 'Sybase Database'), 
                                       ('ssh', 'SSH')])
    config_name = StringField('Configuration Name', validators=[DataRequired()])
    submit = SubmitField('Test Connection')
    
# XML Template with placeholders form
class XMLTemplateForm(FlaskForm):
    template_content = TextAreaField('XML Template with Placeholders (use INPUT1, INPUT2, etc.)', 
                                   validators=[DataRequired()],
                                   render_kw={"rows": 10, "placeholder": "<tradeDate>INPUT1</tradeDate>\n<tradeId>INPUT2</tradeId>"})
    submit = SubmitField('Generate Input Form')

# Dynamic form for XML placeholder inputs
class PlaceholderValueForm(FlaskForm):
    placeholder_name = HiddenField()
    placeholder_value = StringField()

# Form for collecting values for placeholders
class XMLInputsForm(FlaskForm):
    template_content = HiddenField()
    placeholder_values = FieldList(FormField(PlaceholderValueForm), min_entries=0)
    submit = SubmitField('Generate Final XML')
