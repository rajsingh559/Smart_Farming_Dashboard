from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import FarmerProfile

User = get_user_model()

class UserAuthTestCase(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.dashboard_url = reverse('dashboard')
        self.profile_url = reverse('profile')
        
        # Test Credentials
        self.user_data = {
            'username': 'testfarmer',
            'email': 'farmer@test.com',
            'password': 'securepassword123',
            'role': 'farmer'
        }

    def test_user_profile_signal_creation(self):
        """Verify FarmerProfile gets created automatically via post_save signals."""
        user = User.objects.create_user(
            username='autosignal', 
            email='auto@test.com', 
            password='password123',
            role='farmer'
        )
        self.assertTrue(hasattr(user, 'profile'))
        self.assertEqual(user.profile.full_name, 'autosignal')

    def test_user_registration_flow(self):
        """Verify registration view processes form submissions and registers users."""
        form_data = {
            'username': 'newfarmer',
            'email': 'new@test.com',
            'role': 'farmer',
            'password1': 'superpassword123',
            'password2': 'superpassword123'
        }
        response = self.client.post(self.register_url, form_data)
        # Check redirect to login view
        self.assertEqual(response.status_code, 302)
        # Verify user is in DB
        self.assertTrue(User.objects.filter(username='newfarmer').exists())

    def test_dashboard_redirects_unauthenticated_user(self):
        """Verify visiting dashboard redirects logged out users to login screen."""
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_authenticated_user_access_dashboard(self):
        """Verify logged-in user can access the main dashboard."""
        user = User.objects.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password']
        )
        # Login
        self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')

    def test_profile_update_fields(self):
        """Verify users can edit their profile metadata."""
        user = User.objects.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password']
        )
        self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        
        update_data = {
            'first_name': 'Raj',
            'last_name': 'Singh',
            'email': 'newemail@test.com',
            'phone_number': '1234567890',
            'farm_location': 'California',
            'farm_size': 120.5,
            'preferred_crop': 'Almonds'
        }
        response = self.client.post(self.profile_url, update_data)
        self.assertEqual(response.status_code, 302)
        
        # Verify updates in DB
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'Raj')
        self.assertEqual(user.email, 'newemail@test.com')
        self.assertEqual(user.profile.farm_location, 'California')
        self.assertEqual(user.profile.farm_size, 120.5)

    def test_registration_validation_errors(self):
        """Verify registration fails and returns correct error messages when fields are empty."""
        form_data = {
            'username': '',
            'email': '',
            'role': '',
            'password1': '',
            'password2': ''
        }
        response = self.client.post(self.register_url, form_data)
        self.assertEqual(response.status_code, 200)  # Form re-renders with errors
        form = response.context['form']
        self.assertFormError(form, 'username', 'Username is required.')
        self.assertFormError(form, 'email', 'Email is required.')
        self.assertFormError(form, 'role', 'Role is required.')
        self.assertFormError(form, 'password1', 'Password is required.')
        self.assertFormError(form, 'password2', 'Confirm Password is required.')

