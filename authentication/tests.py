from django.test import TestCase
from authentication.models import *
from django.core.exceptions import ValidationError

class UserModelTests(TestCase):

    def test_two_users_with_same_usernames(self):
        try:
            User.objects.create_user(username='ali', email='ali@gmail.com', password='abcd1234')
            User.objects.create_user(username='ali', email='ali2@gmail.com', password='abcd1234')
            self.assertTrue(False)
        except ValidationError as err:
            pass

    def test_two_users_with_same_emails(self):
        try:
            User.objects.create_user(username='ali', email='shit@gmail.com', password='abcd1234')
            User.objects.create_user(username='omid', email='shit@gmail.com', password='abcd1234')
            self.assertTrue(False)
        except ValidationError as err:
            pass

    def test_superuser_no_password(self):
        try:
            User.objects.create_superuser(username='ali', email='shit@gmail.com', password=None)
            self.assertTrue(False)
        except ValidationError as err:
            pass

    def test_none_username(self):
        try:
            User.objects.create_user(username=None, email='shit@gmail.com', password='abcd1234')
            self.assertTrue(False)
        except ValidationError as err:
            pass

    def test_none_email(self):
        try:
            User.objects.create_user(username='ali', email=None, password='abcd1234')
            self.assertTrue(False)
        except ValidationError as err:
            pass

    def test_short_weak_password(self):
        try:
            User.objects.create_user(username='ali', email='shit@gmail.com', password='ali2')
            self.assertTrue(False)
        except ValidationError as err:
            pass

    def test_numeric_weak_password(self):
        try:
            User.objects.create_user(username='ali', email='shit@gmail.com', password='1234')
            self.assertTrue(False)
        except ValidationError as err:
            pass

    def test_invalid_email(self):
        try:
            User.objects.create_user(username='ali', email='shit', password='abcd1234')
            self.assertTrue(False)
        except ValidationError as err:
            pass

    def test_long_username(self):
        try:
            User.objects.create_user(username='kfdkjfdlkflkdsfkjdsfkjds3qe3e9i3ei9329ie9odi320e03-32-e32-e23-e23e-3e3-02e-03e-032', 
                    email='shit@gmail.com', password='abcd1234')
            self.assertTrue(False)
        except ValidationError as err:
            pass
