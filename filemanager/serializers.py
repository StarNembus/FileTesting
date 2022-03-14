from django.forms import FileField
from rest_framework import serializers
from rest_framework.serializers import Serializer

from filemanager.models import Files


class FilesSerializer(serializers.ModelSerializer):
    file = FileField()
    class Meta:
        model = Files
        fields = ['id', 'name', 'description', 'date', 'file']


