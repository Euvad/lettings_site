import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from user_profile.models import Profile


@pytest.mark.django_db
def test_profiles_index_view():
    client = Client()
    response = client.get(reverse("profiles_index"))
    assert response.status_code == 200
    assert "profiles_list" in response.context


@pytest.mark.django_db
def test_profile_view():
    user = User.objects.create(username="testuser")
    profile = Profile.objects.create(user=user, favorite_city="Test City")
    client = Client()
    response = client.get(reverse("profile", args=[user.username]))
    assert response.status_code == 200
    assert response.context["profile"] == profile
