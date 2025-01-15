from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class StudentForm(FlaskForm):
    """
    Form to manage student details.
    """
    first_name = StringField(
        'First Name',
        validators=[DataRequired(), Length(min=2, max=50, message="First name must be between 2 and 50 characters.")]
    )
    last_name = StringField(
        'Last Name',
        validators=[DataRequired(), Length(min=2, max=50, message="Last name must be between 2 and 50 characters.")]
    )
    age = IntegerField(
        'Age',
        validators=[DataRequired(), NumberRange(min=3, max=20, message="Age must be between 3 and 20.")]
    )
    grade = SelectField(
        'Grade',
        choices=[('nursery', 'Nursery'), ('grade_1', 'Grade 1'), ('grade_2', 'Grade 2'), ('grade_3', 'Grade 3'),
                 ('grade_4', 'Grade 4'), ('grade_5', 'Grade 5'), ('grade_6', 'Grade 6')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


class FeeForm(FlaskForm):
    """
    Form to calculate and manage fees.
    """
    student_id = IntegerField(
        'Student ID',
        validators=[DataRequired()]
    )
    include_food = BooleanField('Include Food Fee', default=False)
    include_transport = BooleanField('Include Transport Fee', default=False)
    include_extras = BooleanField('Include Extra Fees', default=False)
    submit = SubmitField('Calculate Fee')


class LoginForm(FlaskForm):
    """
    Form for user login.
    """
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=3, max=20, message="Username must be between 3 and 20 characters.")]
    )
    password = StringField(
        'Password',
        validators=[DataRequired(), Length(min=6, message="Password must be at least 6 characters.")]
    )
    remember_me = BooleanField('Remember Me', default=False)
    submit = SubmitField('Login')


class ExpenseForm(FlaskForm):
    """
    Form to record an expense.
    """
    description = StringField(
        'Expense Description',
        validators=[DataRequired(), Length(min=5, max=100, message="Description must be between 5 and 100 characters.")]
    )
    amount = IntegerField(
        'Amount',
        validators=[DataRequired(), NumberRange(min=1, message="Amount must be greater than 0.")]
    )
    category = SelectField(
        'Category',
        choices=[('utility', 'Utility'), ('salary', 'Salary'), ('misc', 'Miscellaneous')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Add Expense')
