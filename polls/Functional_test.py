from unittest import TestCase
from selenium import webdriver

class FunctionalTest(TestCase):

    def setUp(self):
        prof = webdriver.FirefoxProfile()
        prof.set_preference('browser.startup.homepage', 'about:blank')
        prof.set_preference('startup.homepage_welcome_url', 'about:blank')
        prof.set_preference('startup.homepage_welcome_url.additional', 'about:blank')
        prof.set_preference('browser.startup.homepage_override.mstone', 'ignore')
        self.browser = webdriver.Firefox(prof)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('Busco Ayuda', self.browser.title)