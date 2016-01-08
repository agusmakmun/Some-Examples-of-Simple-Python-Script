###Accessing all post (draft or publish) bassed in django generic with filtering by specific conditions 

Thanks so much: http://stackoverflow.com/a/26752556/3445802

<pre>
class PostListView(ListView):
    model = Post
    template_name = &#39;resource/post_list.html&#39;

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context[&#39;user_favs&#39;] = Post.objects.filter(
                bookmarks__username=self.request.user.username).values_list(
                &#39;id&#39;, flat=True)
        return context
</pre>

Template:
<pre>
{% if item.id in user_favs %}
... Your special code here ...
{% endif %}
</pre>

###My stack
<code>object_list</code> is default to views objects from django <code>generic.ListView</code>

<pre>
class Author_Videos(generic.ListView):
	template_name = &quot;author_list_video.html&quot;
	paginate_by = 6

	def get_queryset(self):
		self.username = self.kwargs[&#39;username&#39;]
		user = User.objects.get(username=self.username)
		self.results_filter = models.Video.objects.filter(author__username=user).published().order_by(&#39;-created&#39;).order_by(&#39;-id&#39;)
		return self.results_filter

	def get_context_data(self, **kwargs):
		context_data = super(Author_Videos, self).get_context_data(**kwargs)
		if self.request.user.is_authenticated():
			context_data[&#39;object_list&#39;] = models.Video.objects.filter(author__username=self.request.user.username).order_by(&#39;-created&#39;).order_by(&#39;-id&#39;)
		context_data[&#39;username_author&#39;] = self.username
		return context_data
</pre>
