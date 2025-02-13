import pytest
from letting.models import Address, Letting
from user_profile.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_address_str():
    address = Address(
        number=123,
        street="Main St",
        city="Anytown",
        state="CA",
        zip_code=12345,
        country_iso_code="USA",
    )
    assert str(address) == "123 Main St"


@pytest.mark.django_db
def test_letting_str():
    address = Address.objects.create(
        number=123,
        street="Main St",
        city="Anytown",
        state="CA",
        zip_code=12345,
        country_iso_code="USA",
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    assert str(letting) == "Test Letting"


@pytest.mark.django_db
def test_profile_str():
    user = User.objects.create(username="testuser")
    profile = Profile.objects.create(user=user, favorite_city="Test City")
    assert str(profile) == "testuser"
