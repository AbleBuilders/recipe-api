from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = "harshraj.rathore@gmail.com",
            password = "password@123"
        )
        self.client.force_login(self.admin_user)
        self.user= get_user_model().objects.create_user(
            email = "test1@example.com", 
            password = "test@123",
            name = "Test User"
            )
        
    def test_users_list(self):
        """ Tests if users are listed on the pages """
        url = reverse("admin:coreo_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

        
    def test_user_change_page(self):
        """ Tests when user change page""" 
        url = reverse("admin:coreo_user_change",args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
    
    def test_create_user_page(self):
        """Tests if create user page works"""
        url=reverse("admin:coreo_user_add")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)