
from django.core.mail import send_mail
from django.conf import settings

def send_forgetpass_mail(email,token):

    subject = 'Your forget password link'
    message = f'Hi  ,You want to change your password .Click on The link to reset your password http://127.0.0.1:8000/changepass/{token}/'
    from_email='fayizcv1@gmail.com'
    recipient_list=[email]
    recipient_list=['fayizcv1@gmail.com']
    
    send_mail(subject, message, from_email, recipient_list)
    print(recipient_list)
    return True
