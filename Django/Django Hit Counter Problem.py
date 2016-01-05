#http://stackoverflow.com/a/1603719/3445802

#models.py
class QuestionView(models.Model):
    question = models.ForeignKey(Question, related_name='questionviews')
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40)
    created = models.DateTimeField(default=datetime.datetime.now())

#views.py
def record_view(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    if not QuestionView.objects.filter(
                    question=question,
                    session=request.session.session_key):
        view = QuestionView(question=question,
                            ip=request.META['REMOTE_ADDR'],
                            created=datetime.datetime.now(),
                            session=request.session.session_key)
        view.save()

    return HttpResponse(u"%s" % QuestionView.objects.filter(question=question).count())
