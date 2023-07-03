from flask import Flask, session
from flask_session import Session
from flask_mail import Mail, Message
from blinker import signal

app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config['SECRET_KEY'] = 'aboba'
app.config['CSRF_ENABLED'] = True

app.config['MAIL_SERVER'] = 'non.existent.net'
app.config['MAIL_PORT'] = 505
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'stephenspielberg@gmail.com'
app.config['MAIL_PASSWORD'] = 'somethingsomething'

mail = Mail(app)

import schedule_app.views