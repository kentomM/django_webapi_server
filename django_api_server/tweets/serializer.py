from rest_framework import serializers

from users.serializer import UserSerializer
from .models import Tweet


class TweetsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        return Tweet.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        if instance.user == self.context["request"].user:
            return super().update(instance, validated_data)
        else:
            error = {"message": "You can not edit another user's post"}
            raise serializers.ValidationError(error)
