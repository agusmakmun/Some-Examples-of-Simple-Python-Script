class SelectionDetailPublicView(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_object(self, code):
        try:
            return Selection.objects.get(code=code)
        except Selection.DoesNotExist:
            raise Http404
        except Selection.MultipleObjectsReturned:
            return Selection.objects.filter(code=code).first()

    """
    curl -X GET \
      -H 'Authorization: Token {header_token_key}' \
      http://localhost:8000/api/v1/selection/get/{selection_code/url_code}
    """

    def get(self, request, code, format=None):
        selection = self.get_object(code)
        serializer = SelectionSerializer(selection)
        candidates = [
            {
                "id": candidate.pk,
                "name": candidate.name,
                "photo": candidate.photo.url,
                "about": candidate.about
            } for candidate in Candidate.objects.filter(selection__code=code)
        ]
        serializer = serializer.data
        # updating the dict from `serializer.data`
        serializer['candidates'] = candidates
        return Response(serializer, status=status.HTTP_200_OK)
