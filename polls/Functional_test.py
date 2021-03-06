from unittest import TestCase

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# from buscoayuda4101 import settings
# from polls.models import TiposDeServicio


class FunctionalTest(TestCase):
    # SERVICE_TYPE = TiposDeServicio(nombre='Reporter')
    USER_NAME = 'username' + str(3)
    PASSWORD = 'Password1234'

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

    def test_1_title(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_2_register_user(self):
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
        username.send_keys(self.USER_NAME)

        password = self.browser.find_element_by_id('id_password')
        password.send_keys(self.PASSWORD)

        saveButton = self.browser.find_element_by_id('id_grabar')
        saveButton.click()

        self.browser.implicitly_wait(30)
        span = self.browser.find_element(By.XPATH, "//span[text()='Peter Parker']")

        self.assertIn('Peter Parker', span.text)

    def test_3_view_detail(self):
        self.browser.get('http://localhost:8000')

        self.browser.implicitly_wait(10)
        span = self.browser.find_element(By.XPATH, "//span[text()='Peter Parker']")
        span.click()
        self.browser.implicitly_wait(30)

        fullName = self.browser.find_element(By.XPATH, "//h2[text()='Peter Parker']")

        self.assertIn('Peter Parker', fullName.text)

    def test_4_login_user(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(5)
        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(5)

        username = self.browser.find_element_by_id('id_username_login')
        username.send_keys(self.USER_NAME)

        password = self.browser.find_element_by_id('id_password_login')
        password.send_keys(self.PASSWORD)

        login_button = self.browser.find_element_by_id('id_login_button')
        login_button.click()

        self.browser.implicitly_wait(5)

        mensajeFlotante = self.browser.find_element_by_class_name('float-message')
        textMensaje = mensajeFlotante.text
        self.assertTrue(textMensaje.index('SUCCESS: Bienvenido al sistema ' + str(self.USER_NAME)))

    def test_5_edit_user(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(5)

        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(5)

        username = self.browser.find_element_by_id('id_username_login')
        username.send_keys(self.USER_NAME)

        password = self.browser.find_element_by_id('id_password_login')
        password.send_keys(self.PASSWORD)

        login_button = self.browser.find_element_by_id('id_login_button')
        login_button.click()

        self.browser.implicitly_wait(5)

        link = self.browser.find_element_by_id('id_editar')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        self.browser.execute_script("arguments[0].value = ''", nombre)
        nombre.send_keys('Eddie')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        self.browser.execute_script("arguments[0].value = ''", apellidos)
        apellidos.send_keys('Brock')

        telefono = self.browser.find_element_by_id('id_telefono')
        self.browser.execute_script("arguments[0].value = ''", telefono)
        telefono.send_keys(999999999)

        correo = self.browser.find_element_by_id('id_correo')
        self.browser.execute_script("arguments[0].value = ''", correo)
        correo.send_keys('Eddie@mail.fake')

        saveButton = self.browser.find_element_by_id('id_grabar')
        saveButton.click()

        logoutButton = self.browser.find_element_by_id('id_logout')
        logoutButton.click()

        self.browser.implicitly_wait(30)
        span = self.browser.find_element(By.XPATH, "//span[text()='Eddie Brock']")

        self.assertIn('Eddie Brock', span.text)

    def test_6_register_comment(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(5)

        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(5)

        username = self.browser.find_element_by_id('id_username_login')
        username.send_keys(self.USER_NAME)

        password = self.browser.find_element_by_id('id_password_login')
        password.send_keys(self.PASSWORD)

        login_button = self.browser.find_element_by_id('id_login_button')
        login_button.click()

        self.browser.implicitly_wait(5)

        link = self.browser.find_element_by_id('id_comment')
        link.click()

        self.browser.implicitly_wait(20)

        texto = self.browser.find_element_by_id('id_texto')
        texto.send_keys('Este es mi comentario')

        comment_email = self.browser.find_element_by_id('id_comment_email')
        comment_email.send_keys('test@gmail.com')

        saveButton = self.browser.find_element_by_id('id_save_comment')
        saveButton.click()


