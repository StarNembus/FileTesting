import mimetypes
import os
from wsgiref.util import FileWrapper
from django.db.migrations import serializer
from django.shortcuts import render
from django.http import FileResponse, StreamingHttpResponse
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework import permissions, status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Files
from .serializers import FilesSerializer


class FilesViewSet(ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    # permission_classes = (permissions.AllowAny,)
    parser_classes = (MultiPartParser, FormParser)

    # def post(self, request):
    #     file = request.FILES.get('file')
    #     content_type = file.content_type
    #     response = "POST API and you have uploaded a {} file".format(content_type)
    #     return Response(response)

    def post(self, request):
        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PassthroughRenderer(renderers.BaseRenderer):
    media_type = ''
    format = ''

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data


@action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
class DownloadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    def download(self, *args, **kwargs):
        instance = self.get_object()
        file_handle = instance.file.open()
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response
