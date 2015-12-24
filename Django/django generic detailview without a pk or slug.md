Refference: http://chriskief.com/2012/12/29/django-generic-detailview-without-a-pk-or-slug/

This automatic for user was loggin.

<pre>
class UserView(DetailView):

    template_name = 'template.html'
    #model = User
    #context_object_name = 'foo'

    def get_object(self):
        return get_object_or_404(User, pk=request.session['user_id'])
</pre>

Also note that the model is no longer necessary as you’re explicitly calling it in get_object. The object is now available in the template using the model name, in this case user:

<pre>{{ user.id }}</pre>

Or like this:

<pre>
from member.models import Member

class Dashboard_Member(generic.DetailView):
	model = Member
	template_name = "dashboard_member.html"

	def get_object(self):
		return get_object_or_404(User, pk=self.request.user.id)
</pre>


Or like this:
<pre>
from member.models import Member

class Dashboard_Member(generic.DetailView):
	template_name = "dashboard_member.html"

	def get_object(self):
		user_loggin = get_object_or_404(User, pk=self.request.user.id)
		return Member.objects.get(username=user_loggin.username, email=user_loggin.email)

</pre>
