from django.test import TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from user.models import User
from django.test import Client


class TestViewCase(TestCase):
    def test_view(self):
        url = reverse('create_post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view02(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        url = reverse('register')
        c = Client()
        response = c.post(url, {'username': 'test01',
                                'email': 'test01@test.tu',
                                'password1': '(1234567890)',
                                'password2': '(1234567890)'
                                })
        self.assertEqual(response.status_code, 302)

    def test_verify_user(self):
        url = reverse('register')
        c = Client()
        c.post(url, {'username': 'test02',
                     'email': 'test02@test.tu',
                     'password1': '(1234567890)',
                     'password2': '(1234567890)'
                     })
        user = User.objects.get(username='test02')
        url_verify = "/users/verify_email/" + user.token + '/' + str(urlsafe_base64_encode(force_bytes(user.pk))) + '/'
        response = c.get(url_verify)
        self.assertEqual(response.url, '/users/addition_info/')

    def test_addition_info(self):
        url = reverse('register')
        c = Client()
        c.post(url, {'username': 'test03',
                     'email': 'test03@test.tu',
                     'password1': '(1234567890)',
                     'password2': '(1234567890)'
                     })
        user = User.objects.get(username='test03')
        url_verify = "/users/verify_email/" + user.token + '/' + str(urlsafe_base64_encode(force_bytes(user.pk))) + '/'
        c.get(url_verify)
        response = c.post('/users/addition_info/', {'bio': 'test bio',
                                                    'first_name': 'test first name',
                                                    'last_name': 'test last name',
                                                    })
        self.assertEqual(response.url, '/post/')

    def test_addition_image(self):
        url = reverse('register')
        c = Client()
        c.post(url, {'username': 'test04',
                     'email': 'test04@test.tu',
                     'password1': '(1234567890)',
                     'password2': '(1234567890)'
                     })
        user = User.objects.get(username='test04')
        url_verify = "/users/verify_email/" + user.token + '/' + str(urlsafe_base64_encode(force_bytes(user.pk))) + '/'
        c.get(url_verify)
        test_file = open('Tests/test_pic.jpg', 'rb')
        response = c.post('/users/addition_info/', {'bio': 'test bio',
                                                    'first_name': 'test first name',
                                                    'last_name': 'test last name',
                                                    'avatar': test_file
                                                    })
        test_file.close()
        user = User.objects.get(username='test04')
        self.assertIsNotNone(user.avatar.url)
