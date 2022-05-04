from flask import Flask, render_template, request, flash, redirect
from form import ContactForm
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)


app.secret_key = 'Secretkey'

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'aram.moh@yandex.com'
app.config['MAIL_PASSWORD'] = 'TAwiq3RUqEVaF2X'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route('/')
def home():
    date = datetime.now().year

    return render_template('home.html', date=date)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    date = datetime.now().year
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form, date=date)
        else:
            msg = Message(form.subject.data, sender='aram.moh@yandex.com',
                          recipients=['mraram77@gmail.com'])

            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return 'Form posted.'

    elif request.method == 'GET':
        return render_template('contact.html', form=form, date=date)


@app.route('/about')
def about():
    date = datetime.now().year
    return render_template('about.html', date=date)


@app.route('/works')
def works():
    date = datetime.now().year
    return render_template('works.html', date=date)


if __name__ == '__main__':
    app.run(debug=True)
