from django.test import TestCase
import json
from users.models import User


class LoggedInTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user("user@example.com", "password")

    def setUp(self) -> None:
        self.client.force_login(self.user)
