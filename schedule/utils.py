from django.core.mail import EmailMessage


def send_email_notification(title, body, to, attachment=None):
    email = EmailMessage(title, body=body, to=to)
    email.content_subtype = 'html'
    if attachment:
        email.attach(attachment['file_name'], attachment['content'], attachment['type'])
    email.send()
