from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from shop.models import Seo


class HomeTestCase(APITestCase):

    def setUp(self):

        self.seo = Seo.objects.create(
            url='main_p',
            title='Страница ',
            description='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf s',
            main_text='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
        )

    def test_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class AboutTestCase(APITestCase):
    def setUp(self):
        self.seo = Seo.objects.create(
            url='about',
            title='Страница о нас',
            description='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf s',
            main_text='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
        )

    def test_about(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTemplateUsed(response, 'content/about.html')
        self.assertEqual(response.context['seo'].url, self.seo.url)
        self.assertEqual(response.context['seo'].title, self.seo.title)
        self.assertEqual(response.context['seo'].description, self.seo.description)
        self.assertEqual(response.context['seo'].main_text, self.seo.main_text)


class ContactsTestCase(APITestCase):
    def setUp(self):
        self.seo = Seo.objects.create(
            url='contacts',
            title='Страница с нашими контактами',
            description='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf s',
            main_text='fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
                      'fgdfdgs dgf sf gdgfds gfd sgfds gfd dgf '
        )

    def test_contacts(self):
        url = reverse('contacts')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTemplateUsed(response, 'content/contacts.html')
        self.assertEqual(response.context['seo'].url, self.seo.url)
        self.assertEqual(response.context['seo'].title, self.seo.title)
        self.assertEqual(response.context['seo'].description, self.seo.description)
        self.assertEqual(response.context['seo'].main_text, self.seo.main_text)
