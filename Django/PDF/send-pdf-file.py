from django.core.mail import EmailMultiAlternatives

msg = EmailMultiAlternatives(subject, html_content, from, [to])
attachment = open("yourpdf.pdf", 'rb')
msg.attach_alternative(html_content, "text/html")
msg.attach("yourpdf.pdf", attachment.read(), 'application/pdf')
msg.send()
