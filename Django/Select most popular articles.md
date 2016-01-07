
####Thanks so much: http://stackoverflow.com/a/10638642/3445802

<pre>
Article.objects.filter(favorited__in=[...]).annotate(
        vc=models.Count('vote')).order_by('-vc')
</pre>

Or normally faster(less joins), but more complex, and limited(no longer a QuerySet but not a big issue normally) sub-query version

<pre>
qs = Article.objects.filter(favorited__in=[...])
top_votes = Vote.objects.filter(article__in=qs).values('article').annotate(
         vc=models.Count('pk')).values_list('article', 'vc').order_by('-vc')

# normally you may only want Top N
top_n_pks = tuple(pk for pk, vc in top_votes[:N])
tops = sorted(Article.objects.filter(pk__in=top_n_pks).order_by(),
         key=lambda x: top_n_pks.index(x.pk))
</pre>

###In my last project
<pre>
class Popular_Videos_Views(generic.ListView):
	template_name = 'popular_videos.html'
	paginate_by = 6

	def get_queryset(self):
		self.queryset = models.Video.objects.published().order_by('-created').order_by('-id')
		"""Count all `Video_Views` with annotate, filtering for all Video."""
		top = models.Video_Views.objects.filter(video__in=self.queryset).values('video').annotate(visit=Count('pk')).order_by('-visit')

		"""See what we have in param: top, it filtering for most popular_videos.
		value `visit`: is many video was visited.
		value `video`: is pk/id from video.

		>>> top_n = tuple(visit for visit in top[:3])
		>>> top_n
		({'visit': 4, 'video': 10}, {'visit': 4, 'video': 11}, {'visit': 3, 'video': 6})
		>>>
		"""

		"""Getting pk/id from video using list generator.
		>>> list_pk_top_video = [ pk['video'] for pk in top[:3] ]
		>>> list_pk_top_video
		[10, 11, 6]
		>>> Video.objects.filter(pk__in=list_pk_top_video)
		[<Video: Relaxing Love Songs>, <Video: Westlife - My Best Boy Band Forever>, <Video: 6 Cool New Technologies and Inventions 2015>]
		#>>>
		"""

		list_pk_top_video = [ pk['video'] for pk in top[:10] ] #to[:10] == video popular 
		"""Getting Videos with filtering by id in `list_pk_top_video`"""
		results_filter_of_top_video = models.Video.objects.filter(pk__in=list_pk_top_video)
		print results_filter_of_top_video

		return results_filter_of_top_video
	
	def pagination(self):
		paginator = Paginator(self.get_queryset(), self.paginate_by) #number of pagination from default sort
		page = self.request.GET.get('page')
		try:
			all_videos = paginator.page(page)
		except PageNotAnInteger:
			all_videos = paginator.page(1)
		except EmptyPage:
			all_videos = paginator.page(paginator.num_pages)

		index = all_videos.number - 1
		limit = 5 #limit for show range left and right of number pages
		max_index = len(paginator.page_range)
		start_index = index - limit if index >= limit else 0
		end_index = index + limit if index <= max_index - limit else max_index
		page_range = paginator.page_range[start_index:end_index]
		return page_range

	def get_context_data(self, **kwargs):
		context_data = super(Popular_Videos_Views, self).get_context_data(**kwargs)
		context_data['page_range'] = self.pagination

		return context_data
</pre>
