from collections import OrderedDict
from datetime import datetime, timezone, timedelta
from unittest import mock
from django.urls import reverse

from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from .views import TweetsViewSet
from .models import Tweet
from users.models import CustomUser as User


def mock_date1():
    return datetime(2019, 4, 1, tzinfo=timezone(timedelta(hours=+9)))


def mock_date2():
    return datetime(2019, 4, 2, tzinfo=timezone(timedelta(hours=+9)))


class TweetsModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.testuser = User.objects.create_user(
            username="test",
            email="test@test.com",
            password="test")
        cls.testuser.save()

        cls.testuser2 = User.objects.create_user(

            username="test2",
            email="test2@test.com",
            password="test")
        cls.testuser2.save()

        cls.factory = APIRequestFactory()

    @mock.patch("django.utils.timezone.now", mock_date1)
    def test_create_tweet(self):
        request = self.factory.post("/api/v1/tweets/", {
            "body": "sample tweet"
        })
        force_authenticate(request, user=self.testuser)
        view = TweetsViewSet.as_view({"post": "create"})
        response = view(request)

        # Status Check
        self.assertEqual(response.status_code, 201)

        # Response Check
        self.assertDictEqual(response.data, {
            "id": 1,
            "body": "sample tweet",
            "created_at": mock_date1().isoformat(),
            "updated_at": mock_date1().isoformat(),
            "user": OrderedDict({
                "id": 1,
                "username": "test"
            })
        })

    @mock.patch("django.utils.timezone.now", mock_date1)
    def test_list_tweet(self, null=None):
        # testuser1のツイートをDB登録
        Tweet.objects.get_or_create({
            "id": 1,
            "body": "I'm test user1",
            "created_at": mock_date1(),
            "updated_at": mock_date1(),
            "user": self.testuser
        })
        # testuser2のツイートをDB登録
        Tweet.objects.get_or_create({
            "id": 2,
            "body": "I'm test user2",
            "created_at": mock_date1(),
            "updated_at": mock_date1(),
            "user": self.testuser2
        })

        # testuser2で認証してアクセス
        request = self.factory.get("api/v1/tweets/")
        force_authenticate(request, user=self.testuser2)
        view = TweetsViewSet.as_view({"get": "list"})
        response = view(request)

        # Status Check
        self.assertEqual(response.status_code, 200)

        # Response Check
        self.assertDictEqual(response.data, {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [{
                "id": 1,
                "user": OrderedDict({
                    "id": 1,
                    "username": "test"
                }),
                "body": "I'm test user1",
                "created_at": mock_date1().isoformat(),
                "updated_at": mock_date1().isoformat(),
            }]
        })

    @mock.patch("django.utils.timezone.now", mock_date1)
    def test_destroy_tweet(self):
        Tweet.objects.get_or_create({
            "id": 1,
            "body": "sample tweet",
            "created_at": mock_date1(),
            "updated_at": mock_date1(),
            "user": self.testuser
        })

        request = self.factory.delete('api/v1/tweets/1/')
        force_authenticate(request, user=self.testuser)
        view = TweetsViewSet.as_view({"delete": "destroy"})
        response = view(request)

        # StatusCheck
        self.assertEqual(response.status_code, 204)

    '''
    @mock.patch("django.utils.timezone.now", mock_date1)
    def test_update_tweet(self):
        Tweet.objects.get_or_create({
            "id": 1,
            "body": "sample tweet",
            "created_at": mock_date1(),
            "updated_at": mock_date1(),
            "user": self.testuser
        })

        request = self.factory.put("/api/v1/tweets/1/", {
            "body": "update tweet",
        })
        force_authenticate(request, user=self.testuser)
        view = TweetsViewSet.as_view({"put": "update"})
        response = view(request)

        # StatusCheck
        self.assertEqual(response.status_code, 200)

        self.assertDictEqual(response.data, {
            "id": 1,
            "body": "update tweet",
            "created_at": mock_date1().isoformat(),
            "updated_at": mock_date2().isoformat(),
            "user": OrderedDict({
                "id": 1,
                "username": "test"
            })
        })
    '''