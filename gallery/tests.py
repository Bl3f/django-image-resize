import os
import shutil

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from gallery.utils import minify_name


class TestUtils(TestCase):
    def test_minify_name_simple(self):
        name = 'Mon chat'
        self.assertEqual(minify_name(name), 'mon_chat')


class TestGalleryViews(TestCase):
    def test_upload_view(self):
        with open('gallery/assets/test_image.jpeg', 'rb') as image:
            url = reverse('upload')

            data = {
                'file': image,
                'name': 'Mon chat',
                'user': 'blef',
            }

            self.client.post(url, data=data)

        expected_file_path = os.path.join(settings.MEDIA_ROOT, 'blef', 'mon_chat.jpeg')
        self.assertTrue(os.path.exists(expected_file_path))

        shutil.rmtree(settings.MEDIA_ROOT)

