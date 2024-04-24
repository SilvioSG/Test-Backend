from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import User

class UserViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'name': 'Test_User',
            'email': 'test@example.com',
            'password_hash': 'password'
        }
        self.user = User.objects.create(**self.user_data)

    def test_get_all_users(self):
        url = reverse('get_all_users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_get_user_by_name_not_found(self):
        url = reverse('get_user_by_name', kwargs={'name': 'Not_Found'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_get_user_by_name(self):
        url = reverse('get_user_by_name', kwargs={'name': self.user.name})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.user.name)
        self.assertEqual(response.data['email'], self.user.email)
        self.assertEqual(response.data['password_hash'], self.user.password_hash)



    def test_create_user(self):
        url = reverse('create_user')
        new_user_data = {
            'name': 'New_User',
            'email': 'new@example.com',
            'password_hash': 'new_password'
        }
        response = self.client.post(url, new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        new_user = User.objects.get(name=new_user_data['name'])
        self.assertEqual(new_user.email, new_user_data['email'])



    def test_create_user_equal_name(self):
        url = reverse('create_user')
        new_user_data = {
            'name': 'Test_User',
            'email': '',
            'password_hash': ''
        }
        response = self.client.post(url, new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



    def test_update_user(self):
        url = reverse('update_user')
        updated_user_data = {
            'name': 'Test_User',
            'email': 'updated@example.com'
        }
        response = self.client.put(url, updated_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, updated_user_data['name'])
        self.assertEqual(self.user.email, updated_user_data['email'])

 
    def test_update_user_not_found(self):
        url = reverse('update_user')
        updated_user_data = {
            'name': 'Not_Found',
            'email': ''}
        response = self.client.put(url, updated_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_user(self):
        url = reverse('delete_user', kwargs={'name': self.user.name})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

    def test_delete_user_not_found(self):
        url = reverse('delete_user', kwargs={'name': 'Not_Found'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    