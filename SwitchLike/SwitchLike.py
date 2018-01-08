from flask import Flask, render_template, request ,flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField

app = Flask(__name__)


@app.route('/home')

def home():
    return render_template('home.html')

@app.route('/balance')

def balance():
    return render_template("balance.html")

@app.route('/promotions')

def promotions():
    return render_template("promotions.html")

if __name__ == '__main__':
    app.run()
