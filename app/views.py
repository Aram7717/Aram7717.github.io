from app import app, mail
from .form import ContactForm
from flask_mail import Mail, Message
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect




def home():
     
    print(f"f'ENV is set to: {app.config['FLASK_ENV']}")
    date = datetime.now().year

    return render_template('home.html', date=date) 


# @app.route('/contact', methods=['GET', 'POST'])
def contact():
    date = datetime.now().year
    form = ContactForm(request.form)
    
    
    if request.method == 'POST':
        if form.validate() == False:
            
            
            return render_template('contact.html', form=form, date=date)

        else:
            
            msg = Message(form.subject.data, recipients=['aram.moh@yandex.com'])

            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            
            mail.send(msg)
            return render_template('sent.html')

    elif request.method == 'GET':
        return render_template('contact.html', form=form, date=date)



# @app.route('/about')
def about():
    date = datetime.now().year
    return render_template('about.html', date=date)


# @app.route('/works')
def works():
    date = datetime.now().year
    return render_template('works.html', date=date)
