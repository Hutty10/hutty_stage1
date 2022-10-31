from rest_framework import serializers

from stageone.models import StageOneUser


class StageOneUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageOneUser
        fields = ["slackUsername", "backend", "age", "bio"]
