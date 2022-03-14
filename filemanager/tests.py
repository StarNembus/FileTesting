from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from filemanager.views import FilesViewSet


class TestToDoView(TestCase):

    def test_get_list(self):
        admin = User.objects.create_superuser('admin', email='test@test.com', password='1')
        factory = APIRequestFactory()
        request = factory.get('/api/files/')
        force_authenticate(request, user=admin)
        view = FilesViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


