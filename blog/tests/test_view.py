from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from blog.views import home_page


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string("blog/home.html", request=request)
        self.assertEqual(response.content.decode(), expected_html)
