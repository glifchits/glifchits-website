'''
Created on 2013-04-30

@author: glifchits
'''
from flask import Flask, render_template, request, redirect, url_for

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/resume/')
    def resume():
        return render_template('resume.html', title_modifier=" - Resume")

    @app.route('/contact/', methods=['GET', 'POST'])
    def contact():
        if request.method == "POST":
            return send_email(request)
        else:
            return render_template('contact.html', title_modifier=" - Contact")

    def send_email(response):
        try:
            my_email = "George Lifchits <george.lifchits@gmail.com>"
            
            the_sender = response.form['sender']
            the_subject = response.form['subject']
            body_text = response.form['message']
        
            if the_subject == "": the_subject = "No subject"
            if body_text == "": body_text = "No body text entered"
            
            the_subject = "(WEBSITE) " + the_subject
            body_text = the_sender + "<br/>" + body_text
            
            from google.appengine.api import mail
            
            message = mail.EmailMessage(sender=my_email, subject=the_subject)
            message.to = my_email
            message.html = body_text
    
            message.send()
            return send_success()
        except:
            return send_success(False)

    def send_success(response = True):
        return render_template('contact.html', send_success = response)

    return app
