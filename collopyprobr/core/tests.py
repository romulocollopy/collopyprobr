# coding: utf-8
from django.test import TestCase

class HomePageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    
    def test_get(self):
        'GET / must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Homepage must use template core/index.tml'
        self.assertTemplateUsed(self.resp, 'core/index.html')


class AboutTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/about/')

    def test_get(self):
        'GET /about/ must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'About must use template core/about.html'
        self.assertTemplateUsed(self.resp, 'core/about.html')


class ContactTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/contact/')

    def test_get(self):
        'GET /contact/ must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'About must use template core/contact.html'
        self.assertTemplateUsed(self.resp, 'core/contact.html')


