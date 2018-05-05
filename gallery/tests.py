from django.test import TestCase
from django.urls import reverse


class TestGalleryViews(TestCase):
    def test_upload_view(self):
        with open('gallery/assets/test_image.jpeg', 'rb') as image:
            url = reverse('upload')

            data = {
                'image': image,
                'name': 'Mon chat',
            }

            self.client.post(url, data=data)
