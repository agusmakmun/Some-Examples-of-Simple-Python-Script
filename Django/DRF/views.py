from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api_evotee.serializer import (UserSerializer, SelectionSerializer,
                                   CandidateSerializer, VoteSerializer)
from api_evotee.permissions import IsOwnerOrReadOnly
from evotee.models import (Selection, Candidate, Vote)


class CandidateListView(APIView):
    parser_classes = (FormParser, MultiPartParser)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get(self, request, format=None):
        """
        curl -X GET \
          -H 'Authorization: Token {header_token_key}' \
          http://localhost:8000/api/v1/candidates
        """
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        curl -X POST -S \
          -H 'Accept: application/json' \
          -H 'Content-Type: multipart/form-data' \
          -H 'Authorization: Token {header_token_key}' \
          -F "selection={selection_code/url_code}" \
          -F "name={candidate name}" \
          -F "about={about}" \
          -F "photo=@/path/to/your_photo.jpg;type=image/jpg" \
          http://localhost:8000/api/v1/candidates
        """
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                selection=Selection.objects.get(code=request.data.get('selection')),
                photo=request.data.get('photo')
            )
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
