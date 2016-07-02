from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):
    def test_can_see_blog_posts(self):
        self.browser.get(self.server_url)

        self.assertIn("Robertab's blog", self.browser.title)
