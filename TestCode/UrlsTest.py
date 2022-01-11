from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Hospital.views import index, doctor, show_doctors, show_profile
from Login.views import login_user, logout_user, create_account

class TestUrls(SimpleTestCase):
    def test_index(self):
        url=reverse(index)
        self.assertEquals(resolve(url))

    def test_index(self):
        url=reverse(doctor)
        self.assertEquals(resolve(url))

    def test_sho_doctors(self):
        url=reverse(show_doctors)
        self.assertEquals(resolve(url))

    def test_showprofile(self):
        url=reverse(show_profile)
        self.assertEquals(resolve(url))
    
    ##########################################

    def test_login_users(self):
        url=reverse(login_user)
        self.assertEquals(resolve(url))

    def test_logout_users(self):
        url=reverse(logout_user)
        self.assertEquals(resolve(url))

    def test_showprofile(self):
        url=reverse(create_account)
        self.assertEquals(resolve(url))    
