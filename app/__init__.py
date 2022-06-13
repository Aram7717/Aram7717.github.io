
from flask import Flask
from config import DevelopmentConfig, ProductionConfig
from flask_mail import Mail


app = Flask(__name__)


app.config.from_object(ProductionConfig)
mail= Mail(app)


from app import views
app.add_url_rule('/', view_func=views.home)
app.add_url_rule('/about', view_func=views.about)
app.add_url_rule('/works', view_func=views.works)
app.add_url_rule('/contact', view_func=views.contact, methods=['GET', 'POST'])