
####Thanks so much: http://stackoverflow.com/a/10638642/3445802

<pre>
Article.objects.filter(favorited__in=[...]).annotate(
        vc=models.Count(&#39;vote&#39;)).order_by(&#39;-vc&#39;)
</pre>

Or normally faster(less joins), but more complex, and limited(no longer a QuerySet but not a big issue normally) sub-query version

<pre>
qs = Article.objects.filter(favorited__in=[...])
top_votes = Vote.objects.filter(article__in=qs).values(&#39;article&#39;).annotate(
         vc=models.Count(&#39;pk&#39;)).values_list(&#39;article&#39;, &#39;vc&#39;).order_by(&#39;-vc&#39;)

# normally you may only want Top N
top_n_pks = tuple(pk for pk, vc in top_votes[:N])
tops = sorted(Article.objects.filter(pk__in=top_n_pks).order_by(),
         key=lambda x: top_n_pks.index(x.pk))
</pre>

###In my last project
<pre>
class Popular_Videos_Views(generic.ListView):
	template_name = &#39;popular_videos.html&#39;
	paginate_by = 6

	def get_queryset(self):
		self.queryset = models.Video.objects.published().order_by(&#39;-created&#39;).order_by(&#39;-id&#39;)
		&quot;&quot;&quot;Count all `Video_Views` with annotate, filtering for all Video.&quot;&quot;&quot;
		top = models.Video_Views.objects.filter(video__in=self.queryset).values(&#39;video&#39;).annotate(visit=Count(&#39;pk&#39;)).order_by(&#39;-visit&#39;)

		&quot;&quot;&quot;See what we have in param: top, it filtering for most popular_videos.
		value `visit`: is many video was visited.
		value `video`: is pk/id from video.

		&gt;&gt;&gt; top_n = tuple(visit for visit in top[:3])
		&gt;&gt;&gt; top_n
		({&#39;visit&#39;: 4, &#39;video&#39;: 10}, {&#39;visit&#39;: 4, &#39;video&#39;: 11}, {&#39;visit&#39;: 3, &#39;video&#39;: 6})
		&gt;&gt;&gt;
		&quot;&quot;&quot;

		&quot;&quot;&quot;Getting pk/id from video using list generator.
		&gt;&gt;&gt; list_pk_top_video = [ pk[&#39;video&#39;] for pk in top[:3] ]
		&gt;&gt;&gt; list_pk_top_video
		[10, 11, 6]
		&gt;&gt;&gt; Video.objects.filter(pk__in=list_pk_top_video)
		[&lt;Video: Relaxing Love Songs&gt;, &lt;Video: Westlife - My Best Boy Band Forever&gt;, &lt;Video: 6 Cool New Technologies and Inventions 2015&gt;]
		#&gt;&gt;&gt;
		&quot;&quot;&quot;

		list_pk_top_video = [ pk[&#39;video&#39;] for pk in top[:10] ] #to[:10] == video popular 
		&quot;&quot;&quot;Getting Videos with filtering by id in `list_pk_top_video`&quot;&quot;&quot;
		results_filter_of_top_video = models.Video.objects.filter(pk__in=list_pk_top_video)
		print results_filter_of_top_video

		return results_filter_of_top_video
	
	def pagination(self):
		paginator = Paginator(self.get_queryset(), self.paginate_by) #number of pagination from default sort
		page = self.request.GET.get(&#39;page&#39;)
		try:
			all_videos = paginator.page(page)
		except PageNotAnInteger:
			all_videos = paginator.page(1)
		except EmptyPage:
			all_videos = paginator.page(paginator.num_pages)

		index = all_videos.number - 1
		limit = 5 #limit for show range left and right of number pages
		max_index = len(paginator.page_range)
		start_index = index - limit if index &gt;= limit else 0
		end_index = index + limit if index &lt;= max_index - limit else max_index
		page_range = paginator.page_range[start_index:end_index]
		return page_range

	def get_context_data(self, **kwargs):
		context_data = super(Popular_Videos_Views, self).get_context_data(**kwargs)
		context_data[&#39;page_range&#39;] = self.pagination

		return context_data
</pre>
