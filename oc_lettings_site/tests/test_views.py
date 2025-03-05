import pytest
from django.urls import reverse
from django.test import Client
from letting.models import Address, Letting
from user_profile.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_index_view():
    client = Client()
    response = client.get(reverse("index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_lettings_index_view():
    client = Client()
    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200
    assert "lettings_list" in response.context


@pytest.mark.django_db
def test_letting_view():
    address = Address.objects.create(
        number=123,
        street="Main St",
        city="Anytown",
        state="CA",
        zip_code=12345,
        country_iso_code="USA",
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    client = Client()
    response = client.get(reverse("letting", args=[letting.id]))
    assert response.status_code == 200
    assert response.context["title"] == letting.title
    assert response.context["address"] == letting.address


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
