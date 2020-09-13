import json

from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {'username': 'testcase', 'email': 'test@email.com', 'first_name': 'testcase', 'last_name': 'testcase',
                'about': 'testcast', 'password': "some_strong_psw123"}
        response = self.client.post('/api/user/registration/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UsersViewSetTestCase(APITestCase):

    def setUp(self):
        data = {'username': 'testcase', 'email': 'test@email.com', 'first_name': 'testcase', 'last_name': 'testcase',
                'about': 'testcast', 'password': "some_strong_psw123"}
        self.user = self.client.post('/api/user/registration/', data)
        # get web token JSON for newly created user
        response = self.client.post('/api/token-auth/', data={'username': 'testcase', 'password': 'some_strong_psw123'})
        self.token = response.data['token']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def test_users_list_authenticated(self):
        response = self.client.get('/api/user/all_users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_list_un_autenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/user/all_users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_detail_retrieve(self):
        response = self.client.get('/api/user/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testcase')

    def test_user_data_update_by_owner(self):
        data = {'username': 'testcase', 'about': 'about test case', 'first_name': 'Test',
                "last_name": 'Case'}
        response = self.client.put('/api/user/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {'id': 1, 'username': 'testcase', 'first_name': 'Test', 'last_name': 'Case',
                          'about': 'about test case', 'email': 'test@email.com'})

    def test_user_account_delete_by_owner(self):
        response = self.client.delete('/api/user/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_data_update_by_random_user(self):
        random_user = CustomUser.objects.create_user(username='random', password='psw1345123451')
        self.client.force_authenticate(user=random_user)
        data = {'username': 'testcase123', 'about': 'about test case123', 'first_name': 'Test123',
                "last_name": 'Case'}
        response = self.client.put('/api/user/1/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_data_update_by_admin(self):
        admin = CustomUser.objects.create_superuser(username='admin', password='psw1345123451')
        self.client.force_authenticate(user=admin)
        data = {'username': 'testcase123', 'about': 'about test case123', 'first_name': 'Test123',
                "last_name": 'Case'}
        response = self.client.put('/api/user/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {'id': 1, 'username': 'testcase123', 'first_name': 'Test123', 'last_name': 'Case',
                          'about': 'about test case123', 'email': 'test@email.com'})

    def test_user_account_delete_by_admin(self):
        admin = CustomUser.objects.create_superuser(username='admin', password='psw1345123451')
        self.client.force_authenticate(user=admin)
        response = self.client.delete('/api/user/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)