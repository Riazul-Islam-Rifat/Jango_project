from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse
from Hospital.views import index, Patient, doctor
from Login.views import login_user, logout_user, create_account
import json

class TestViews(TestCase):
    
    def test_index(self):
        client=Client()
        response=client.get(reverse(index))
        self.assertEquals(response.ststus_code,200)
        self.assertTemplateUsed(response, 'Hospital/index')

    def test_patient(self):
        client=Client()
        response=client.get(reverse(Patient))
        self.assertEquals(response.ststus_code,200)
        self.assertTemplateUsed(response, 'Hospital/patient')    

    def test_doctor(self):
        client=Client()
        response=client.get(reverse(doctor))
        self.assertEquals(response.ststus_code,200)
        self.assertTemplateUsed(response, 'Hospital/doctor')      

    def test_login_user(self):
        client=Client()
        response=client.get(reverse(login_user))
        self.assertEquals(response.ststus_code,200)
        self.assertTemplateUsed(response, 'Login/login_user')

    def test_logout_user(self):
        client=Client()
        response=client.get(reverse(logout_user))
        self.assertEquals(response.ststus_code,200)
        self.assertTemplateUsed(response, 'Login/logout_user')    

    def test_create_account(self):
        client=Client()
        response=client.get(reverse(create_account))
        self.assertEquals(response.ststus_code,200)
        self.assertTemplateUsed(response, 'Login/create_account')       