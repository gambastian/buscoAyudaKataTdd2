from unittest import TestCase

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# from buscoayuda4101 import settings
# from polls.models import TiposDeServicio


class FunctionalTest(TestCase):
    # SERVICE_TYPE = TiposDeServicio(nombre='Reporter')

    def setUp(self):
        # settings.configure()
        # self.SERVICE_TYPE.save()
        prof = webdriver.FirefoxProfile()
        prof.set_preference('browser.startup.homepage', 'about:blank')
        prof.set_preference('startup.homepage_welcome_url', 'about:blank')
        prof.set_preference('startup.homepage_welcome_url.additional', 'about:blank')
        prof.set_preference('browser.startup.homepage_override.mstone', 'ignore')
        self.browser = webdriver.Firefox(prof)

    def tearDown(self):
        # self.SERVICE_TYPE.delete()
        self.browser.quit()

    def test_title(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_register_user(self):
        self.browser.get("http://localhost:8000")
        link = self.browser.find_element_by_id('id_register');
        link.click()
        self.browser.implicitly_wait(5)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Peter')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Parker')

        aniosExperiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        aniosExperiencia.send_keys(10)

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Reporter']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys(3111234)

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('test@mail.fake')

        username = self.browser.find_element_by_id('id_username')
        username.send_keys('username2')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('Password1234')

        saveButton = self.browser.find_element_by_id('id_grabar')
        saveButton.click()

        self.browser.implicitly_wait(30)
        span = self.browser.find_element(By.XPATH, "//span[text()='Peter Parker']")

        self.assertIn('Peter Parker', span.text)

    def test_view_detail(self):
        self.browser.get('http://localhost:8000')

        self.browser.implicitly_wait(10)
        span = self.browser.find_element(By.XPATH, "//span[text()='Peter Parker']")
        span.click()
        self.browser.implicitly_wait(30)

        fullName = self.browser.find_element(By.XPATH, "//h2[text()='Peter Parker']")

        self.assertIn('Peter Parker', fullName.text)

    def test_login_user(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(5)
        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(5)

        username = self.browser.find_element_by_id('id_username')
        username.send_keys('username2')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('Password1234')

        login_button = self.browser.find_element_by_id('id_login_button')
        login_button.click()

        self.browser.implicitly_wait(20)

        mensajeFlotante = self.browser.find_element_by_class_name('float-message')
        textMensaje = mensajeFlotante.text
        self.assertTrue(textMensaje.index('SUCCESS: Bienvenido al sistema username2'))
