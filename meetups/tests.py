from django.test import TestCase, SimpleTestCase
from django.http import HttpRequest
# Create your tests here.

from  . import views


class EndpointTests(TestCase):
    '''Test the view module'''

    def test_meetup_details_template(self):
        req = HttpRequest()
        re = self.client.get('/meetups/second-meetup')
        self.assertTemplateUsed(re, 'meetups/meetup-details.html')
    
    def test_meetup_details_response(self):
        req = HttpRequest()
        re = self.client.get('/meetups/second-meetup')
        self.assertEqual(re.status_code, 200)
    
    def test_meetups_template(self):
        req = HttpRequest()
        re = self.client.get('/meetups/')
        self.assertTemplateUsed(re, 'meetups/index.html')

    def test_meetups_response(self):
        req = HttpRequest()
        re = self.client.get('/meetups/')
        self.assertEqual(re.status_code, 200)

    # no template, redirecting to /meetups/
    def test_root_template(self):
        req = HttpRequest()
        re = self.client.get('')
        self.assertTemplateNotUsed (re, 'meetups/index.html')

    def test_root_response(self):
        req = HttpRequest()
        re = self.client.get('')
        self.assertEqual(re.status_code, 302)

