####Original Posts: https://python.web.id/blog/adding-broadcast-mail-to-all-user-registered-in-django-admin/

<p>Adding BroadCast Mail to All User Registered in Django Admin. This is my last problem, we need custom default Django Admin to can submit BroadCast mail to All User. Because this is perfectly to make a promotions.</p>

<p>This problem has been helped by our <em>Danny W. Adair</em> who are answered&nbsp;someone&#39;s question about the &quot;<a href="http://stackoverflow.com/a/5803941/3445802" target="_blank">Django Admin Customizing</a>&quot;.</p>

<p>Thereis script of my last project:</p>

<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;">►&nbsp;Makesure in your <code>settings.py</code> was configured for your email backends, egg like this:</div>

<pre>
EMAIL_HOST = &#39;smtp.gmail.com&#39;
EMAIL_PORT = 587
EMAIL_HOST_USER = &#39;your_email@gmail.com&#39;
EMAIL_HOST_PASSWORD = &#39;your_password_email&#39;
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = &#39;django.core.mail.backends.smtp.EmailBackend&#39;</pre>

<p><strong>1.</strong> In your <code>models.py</code></p>

<pre>
class BroadCast_Email(models.Model):
    subject = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    message = RichTextUploadingField()

    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = &quot;BroadCast Email to all Member&quot;
        verbose_name_plural = &quot;BroadCast Email&quot;</pre>

<p><strong>2.</strong> In your <code>admin.py</code>, importing some module for <em>&quot;admin&quot;</em> and for <em>&quot;email setup&quot;</em>.</p>

<pre>
from django.contrib import admin
from django.utils.safestring import mark_safe
import threading
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import (send_mail, BadHeaderError, EmailMessage)
from django.contrib.auth.models import User

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(self.subject, self.html_content, settings.EMAIL_HOST_USER, self.recipient_list)
        msg.content_subtype = &quot;html&quot;
        try:
            msg.send()
        except BadHeaderError:
            return HttpResponse(&#39;Invalid header found.&#39;)

class BroadCast_Email_Admin(admin.ModelAdmin):
    model = models.BroadCast_Email

    def submit_email(self, request, obj): #`obj` is queryset, so there we only use first selection, exacly obj[0]
        list_email_user = [ p.email for p in User.objects.all() ] #: if p.email != settings.EMAIL_HOST_USER   #this for exception
        obj_selected = obj[0]
        EmailThread(obj_selected.subject, mark_safe(obj_selected.message), list_email_user).start()
    submit_email.short_description = &#39;Submit BroadCast (1 Select Only)&#39;
    submit_email.allow_tags = True

    actions = [ &#39;submit_email&#39; ]

    list_display = (&quot;subject&quot;, &quot;created&quot;)
    search_fields = [&#39;subject&#39;,]

admin.site.register(models.BroadCast_Email, BroadCast_Email_Admin)</pre>

<p><strong>3.</strong> And then, you can see. we have <em><strong>&quot;Submit BroadCast&quot;</strong></em> selection, just click button <em><strong>&quot;Go&quot;</strong></em> to submit broadcast mail.</p>

<p><img alt="Results BroadCast Email Configurations in Django Admin" src="https://python.web.id/media/uploads/agaust/2016/02/06/broadcast-email-for-django-admin.png" style="max-width:100%" title="Results BroadCast Email Configurations in Django Admin" /></p>
