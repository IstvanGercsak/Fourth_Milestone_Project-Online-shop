from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class AccountsTesCase(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    # Testing the views

    def test_admin_site(self):
        page = self.client.get("/admin/login/")
        self.assertEqual(page.status_code, 200)

    def test_arrive_at_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_login(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

    def test_arrive_at_register_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")

    def test_arrive_at_profile_page(self):
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")

    # Ask the mentor about this
    def test_logout_page(self):
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        page = self.client.get("/accounts/logout/")
        self.assertRedirects(page, '/', status_code=302)

    def test_404page(self):
        page = self.client.get("/accounts/test123/")
        self.assertEqual(page.status_code, 404)
        self.assertTemplateUsed(page, "404.html")

    def test_password_reset(self):
        page = self.client.get("/accounts/password-reset/")
        self.assertEqual(page.status_code, 200)

    def test_edit(self):
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/accounts/profile/edit/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit.html")

    def test_change_password(self):
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/accounts/profile/change-password/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "change-password.html")
