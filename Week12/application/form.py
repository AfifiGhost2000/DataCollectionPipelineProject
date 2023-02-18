from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UserInputForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    phonenumber = StringField('Phonenumber', validators=[DataRequired()])
    gender = SelectField('Gender', validators = [DataRequired()], 
                        choices = [('Male', 'Male'),
                                   ('Female', 'Female')] 
                        )
    satisfactionrate = SelectField('Satisfaction Rate', validators = [DataRequired()], 
                        choices = [('1', 1),
                                   ('2', 2),
                                   ('3', 3),
                                   ('4', 4),
                                   ('5', 5)              
                                   ] 
                        )
    income = IntegerField('Avg Monthly Income(in USD)', validators=[DataRequired()])
    
    submit = SubmitField("Add Client")


class PredictUserInputForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    
    gender = SelectField('Gender', validators = [DataRequired()], 
                        choices = [('Male', 'Male'),
                                   ('Female', 'Female')] 
                        )
    satisfactionrate = SelectField('Satisfaction Rate', validators = [DataRequired()], 
                        choices = [('1', 1),
                                   ('2', 2),
                                   ('3', 3),
                                   ('4', 4),
                                   ('5', 5)              
                                   ] 
                        )

    
    predict = SubmitField("Predict Income")




    
                         
    
            


