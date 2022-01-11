from os import name
from django.http import response
from django.test import TestCase
from Hospital.models import Patient, Doctor, Emergency_Cabin

class testModels(TestCase):

    def test_patient(self):
        self.patient1= Patient.objects.create(
            name='Rifat'
        )
        self.assertEqual(response.status_code,200)

    def test_patient(self):
        self.Doctor1=Doctor.objects.create(
            fees='1500',
            verified='Verified',
            qualification='MBBS'
        )    
        self.assertEqual(response.status_code,200)

    def test_patient(self):
        self.cabin=Emergency_Cabin.objects.create(
            availibility='yes/no'
        )    
        self.assertEqual(response.status_code,200)