from django.core.mail import send_mail
from django.template import loader

from CS4227_Project.settings import EMAIL_HOST_USER, SERVER_PORT, SERVER_HOST


def send_activate_email(username, receiver_email, token):
    subject = 'CS4227 Project | Activate Account'
    from_email = EMAIL_HOST_USER
    recipient_list = [receiver_email, ]
    data = {
        'username': username,
        'activate_url': 'http://{}:{}/user/activate/?token={}'.format(SERVER_HOST, SERVER_PORT, token),
    }
    html_message = loader.get_template('user/activate_message.html').render(data)
    send_mail(subject=subject, message="",
              from_email=from_email, recipient_list=recipient_list,
              fail_silently=False, html_message=html_message)

