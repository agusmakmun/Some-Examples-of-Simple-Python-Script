from django.core.mail import EmailMessage
subject = "This is subject"
message = "<html><head></head><body>This is body message</body></html>"

def send_email(to_list, subject, message, sender="Aircourts <noreply@aircourts.com>"):
    msg = EmailMessage(subject, message, sender, to_list)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send() #replace 'return' if you use like a form or something else.

#Ref: http://masnun.com/2014/01/09/django-sending-html-only-email.html
