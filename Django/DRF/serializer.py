from rest_framework import serializers
from evotee.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    selection = serializers.CharField(
        source='selection.code',
        read_only=True
    )
    photo = serializers.ImageField(
        max_length=None,
        use_url=True
    )

    class Meta:
        model = Candidate
        fields = ('selection', 'name', 'photo', 'about')

    def create(self, validated_data):
        return Candidate.objects.create(**validated_data)
