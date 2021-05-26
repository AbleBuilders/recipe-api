from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_email_successful(self):
        """ Test for creating user with email successfully""" 
        email= "harshraj.rathore@gmail.com"
        password = "password@123"
        user = get_user_model().objects.create_user(
            email = email, 
            password = password
            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """ Normalizes the email"""
        email = "harshraj.rathore@GMAIL.com"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_invalid_email(self):
        """ Tests if user email address is valid."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_creating_superuser(self):
        """ Creates superuser admin"""
        user = get_user_model().objects.create_superuser(
            "harshraj.rathore@gmail.com",
            "password@123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)