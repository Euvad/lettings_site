import pytest
from django.urls import reverse
from django.test import Client
from letting.models import Address, Letting


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
