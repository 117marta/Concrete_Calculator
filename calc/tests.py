from django.test import TestCase
import pytest
from calc.models import Concrete
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Create your tests here.


# @pytest.mark.django_db
# def test_add_conrete(client, add_concrete):
#     response = client.get('/add_concrete/')
#     assert response.status_code == 200
#     assert response.context['name'] == 'beton'
#     assert response.context['description'] == 'opis'


# Dodanie nowego betonu do BD - OK
# @pytest.mark.django_db
# def test_add_concrete(client, add_concrete):
#     response = client.post('/add_concrete/', {'name': 'beton', 'description': 'opis'})
#     assert response.status_code == 302
#     c = Concrete.objects.get(name='beton')
#     assert c.description == 'opis'


# unauthenticated client
@pytest.mark.django_db
def test_login(client):
    client.login(username="test_user1", password='12345')
    response = client.get('/login/', follow=True)
    assert response.status_code == 200
# follow=True in either of these, the response.status_code will equal the return code of the page after the redirect, rather than the access to the original URL. Therefore, it should resolve to 200, not 301.


# logged-in admin_client
@pytest.mark.django_db
def test_login_v2(admin_client):
    response = admin_client.get('/login/', follow=True)
    assert response.status_code == 200


# Wylogowanie użytkownika
@pytest.mark.django_db
def test_logout(client):
    client.logout()
    response = client.get('/logout/')
    assert response.status_code == 302


# Osoby w CONTACT alfabetycznie
@pytest.mark.django_db
def test_person_contact(client, contact_four_person):
    response = client.get('/contact/')
    assert response.status_code == 200
    p1 = response.context['persons_in_work'][0]
    p2 = response.context['persons_in_work'][1]
    p3 = response.context['persons_in_work'][2]
    p4 = response.context['persons_in_work'][3]
    assert p1.first_name == 'Anna'
    assert p2.first_name == 'Dawid'
    assert p3.first_name == 'Katarzyna'
    assert p4.first_name == 'Zdzisław'


# Dodawanie betonu do bazy z PERMISSION
@pytest.mark.django_db
def test_add_concrete_with_permission(client, user_with_permission):
    client.login(username=user_with_permission.username, password=user_with_permission.password)
    url = '/add_concrete/'
    response = client.get(url)
    assert response.status_code == 302


def test_shape(client):
    response = client.get('/calculate/rectangle')
    assert response.status_code == 301


def test_footing(client):
    response = client.get('/calculate/footing')
    assert response.status_code == 301


def test_cylinder(client):
    response = client.get('/calculate/cylinder')
    assert response.status_code == 301


# @pytest.mark.django_db
# def test_permission(django_user_model):
#     conrete = django_user_model.objects.create(username='bet', password='xyz')
#     # Get or create the permission to set on user
#     ct = ContentType.objects.get(app_label='auth', model='user')
#     p = Permission.objects.get_or_create(content_type=ct, codename='add_concrete', name="Can add concrete")
#     # User don't have the permission
#     assert conrete.has_perm(p) is False
#     # Set permission to user
#     conrete.user_permissions.add(p)
#     assert conrete.has_perm('auth.add_concrete') is True


