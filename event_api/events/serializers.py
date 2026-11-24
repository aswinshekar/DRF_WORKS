

from events.models import Event

from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields="__all__"
        read_only_fields=['id','organizer_id','created']