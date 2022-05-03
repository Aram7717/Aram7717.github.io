from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators, ValidationError


class ContactForm(Form):
    name = StringField("Name", validators=[validators.InputRequired("Please enter your name."
                                                                    )])

    email = StringField("Email", validators=[validators.InputRequired("Please enter your email."
                                                                      ),  validators.Email("Please enter your email address.")])

    subject = StringField(
        "Subject", validators=[validators.InputRequired("Please enter your subject."
                                                        )])

    message = TextAreaField(
        "Message", validators=[validators.InputRequired("Please enter your message."
                                                        )])

    submit = SubmitField("Send")
