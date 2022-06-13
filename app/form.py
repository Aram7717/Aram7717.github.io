from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[validators.DataRequired("Enter your name")])

    email = StringField("Email", validators=[validators.DataRequired("Enter your email address"),
    validators.Email('Enter your email address')])

    subject = StringField(
        "Subject", validators=[validators.DataRequired("Enter your subject")])

    message = TextAreaField(
        "Message", validators=[validators.DataRequired("Enter your message")])

    submit = SubmitField("Send")
