'''
Created on 2013-04-30

@author: glifchits
'''
from flask import Flask, render_template

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/resume/')
    def resume():
        return render_template('resume.html', title_modifier=" - Resume")

    @app.route('/contact/')
    def contact():
        return render_template('contact.html', title_modifier=" - Contact")

    return app