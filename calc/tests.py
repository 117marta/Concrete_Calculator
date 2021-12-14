from django.test import TestCase
import pytest
import datetime
from unittest import mock
import pytz
from calc.models import List
from calc.forms import RectangleForm


# Create your tests here.


# @pytest.mark.django_db
# def test_add_concrete(client, add_concrete):
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


# Strona główna
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_rectangle_get(client):
    response = client.get('/calculate/rectangle/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_rectangle_post(client, add_rectangle):
    response = client.post(f'/concrete/{add_rectangle.pk}/', {'shape': 'Płyta_fund', 'volume': 5})
    assert response.status_code == 200
    print(response.context)
    # assert response.context['shape'] == 'Płyta_fund'
    rectangle = List.objects.get(shape='Płyta_fund')
    assert rectangle.volume == 5


@pytest.mark.django_db
def test_rectangle_post2(client, add_rectangle):
    response = client.post(f'/concrete/{add_rectangle.pk}/', {'X': 1, 'Y': 5, 'Z': 0.3})
    assert response.status_code == 200
    # print(response.context)
    # assert response.context['shape'] == 'Płyta_fund'
    # rectangle = List.objects.get(shape='Płyta_fund')
    # assert response.context['X'].X == 1
    form = RectangleForm(data={'X': 3, 'Y': 5, 'Z': 0.3})
    assert form.is_valid() is True


def test_formularz():
    form = RectangleForm(data={})
    assert form.is_valid() is False


def test_formularz2():
    form = RectangleForm(data={'X': 3, 'Y': 5, 'Z': 0.3})
    assert form.is_valid() is True








# Osoby w "Contact" alfabetycznie
@pytest.mark.django_db
def test_person_contact(client, contact_four_persons):
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


# Dodawanie betonu do bazy z permission "calc.add_concrete"
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


# SUMMARY
@pytest.mark.django_db
def test_summary_show(client, summary_show):
    response = client.get(f'/summary/{summary_show.id}/')
    assert response.status_code == 200
    assert response.context['summary'].shape == 'Kształt'
    assert response.context['summary'].volume == 1234
    assert response.context['summary'].concrete == 'C30/37'
    assert response.context['summary'].use_of_concrete == 'Fundamenty'
    assert response.context['summary'].comment == 'Kozia Wólka 521'
    assert response.context['summary'].legal_name == 'Kamil Chrzanowski'
    assert response.context['summary'].phone == '500600700'
    assert response.context['summary'].concrete_pomp == True
    # assert response.context['summary'].created_date == datetime.datetime.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    # assert response.context['summary'].created_date == datetime.date('%Y-%m-%dT%H:%M:%S.%fZ')
    # mocked = datetime.datetime(2021, 12, 13, 19, 19, 19, tzinfo=pytz.utc)
    # with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
    #     assert response.context['summary'].created_date == mocked
    # testtime = datetime.datetime.strptime('2015-10-31', '%Y-%m-%d')

# @pytest.mark.django_db
# def test_get_registration_date(client, summary_show):
#     response = client.get(f'/summary/{summary_show.id}/')
#     mocked = datetime.datetime(2021, 12, 14, 18, 55, 14, 256496, tzinfo=pytz.utc)
#     with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
#         assert response.context['summary'].created_date == mocked

