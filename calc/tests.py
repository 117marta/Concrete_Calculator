from django.test import TestCase
import pytest
from calc.models import List
from calc.forms import RectangleForm, FootingForm, CylinderForm, TriangleForm, SlabForm, StairsForm, TypeValueForm
from math import pi


# Create your tests here.


# Form - Rectangle, Triangle
@pytest.mark.parametrize(
    'X, Y, Z, validity',
    (
            (3, 4, 1, True),  # Integer
            (1.3, 1.4, 1.1, True),  # Float
            ('jakiś_tekst', 1.4, 1.1, False),  # String
            (1.3, 'jakiś_tekst', 1.1, False),  # String
            (1.3, 1.4, 'jakiś_tekst', False),  # String
            (-1.3, 1.4, 1.1, False),  # Negative number
            (1.3, -1.4, 1.1, False),  # Negative number
            (1.3, 1.4, -1.1, False),  # Negative number
    )
)
def test_rectangle_triangle_form(X, Y, Z, validity):
    form = RectangleForm(data={'X': X, 'Y': Y, 'Z': Z})
    form2 = TriangleForm(data={'X': X, 'Y': Y, 'Z': Z})
    assert form.is_valid() is validity
    assert form2.is_valid() is validity


# Form - Footing
@pytest.mark.parametrize(
    'X, Y, Z, W, validity',
    (
            (10, 10, 5, 2, True),  # Integer
            (10.1, 10.2, 5.3, 2.4, True),  # Float
            ('jakiś_tekst', 10.2, 5.3, 2.4, False),  # String
            (10.1, 'jakiś_tekst', 5.3, 2.4, False),  # String
            (10.1, 10.2, 'jakiś_tekst', 2.4, False),  # String
            (10.1, 10.2, 10.3, 'jakiś_tekst', False),  # String
            (-10.1, 10.2, 5.3, 2.4, False),  # Negative number
            (10.1, -10.2, 5.3, 2.4, False),  # Negative number
            (10.1, 10.2, -5.3, 2.4, False),  # Negative number
            (10.1, 10.2, 5.3, -2.4, False),  # Negative number
    )
)
def test_footing_form(X, Y, Z, W, validity):
    form = FootingForm(data={'X': X, 'Y': Y, 'Z': Z, 'W': W})
    assert form.is_valid() is validity


# Form - Cylinder
@pytest.mark.parametrize(
    'Z, R, validity',
    (
            (5, 2, True),  # Integer
            (5.8, 2.3, True),  # Float
            ('jakiś_tekst', 2.3, False),  # String
            (5.8, 'jakiś_tekst', False),  # String
            (-5.8, 2.3, False),  # Negative number
            (5.8, -2.3, False),  # Negative number
    )
)
def test_cylinder_form(Z, R, validity):
    form = CylinderForm(data={'Z': Z, 'R': R})
    assert form.is_valid() is validity


# Form - Slab
@pytest.mark.parametrize(
    'X, Y, Z, W, H, validity',
    (
            (10, 10, 5, 2, 2, True),  # Integer
            (10.1, 10.2, 5.3, 2.4, 2.5, True),  # Float
            ('jakiś_tekst', 10.2, 5.3, 2.4, 2.5, False),  # String
            (10.1, 'jakiś_tekst', 5.3, 2.4, 2.5, False),  # String
            (10.1, 10.2, 'jakiś_tekst', 2.4, 2.5, False),  # String
            (10.1, 10.2, 10.3, 'jakiś_tekst', 2.5, False),  # String
            (10.1, 10.2, 10.3, 2.4, 'jakiś_tekst', False),  # String
            (-10.1, 10.2, 5.3, 2.4, 2.5, False),  # Negative number
            (10.1, -10.2, 5.3, 2.4, 2.5, False),  # Negative number
            (10.1, 10.2, -5.3, 2.4, 2.5, False),  # Negative number
            (10.1, 10.2, 5.3, -2.4, 2.5, False),  # Negative number
            (10.1, 10.2, 5.3, 2.4, -2.5, False),  # Negative number
    )
)
def test_slab_form(X, Y, Z, W, H, validity):
    form = SlabForm(data={'X': X, 'Y': Y, 'Z': Z, 'W': W, 'H': H})
    assert form.is_valid() is validity


# Form - Stairs
@pytest.mark.parametrize(
    'X, Y, Z, V, W, validity',
    (
            (10, 2, 2, 20, 1, True),  # Integer
            (10.1, 0.2, 0.3, 20, 0.1, True),  # Float, but V must be Integer
            ('jakiś_tekst', 0.2, 0.3, 20, 0.1, False),  # String
            (10.1, 'jakiś_tekst', 0.3, 20, 0.1, False),  # String
            (10.1, 0.2, 'jakiś_tekst', 20, 0.1, False),  # String
            (10.1, 0.2, 0.3, 'jakiś_tekst', 0.1, False),  # String
            (10.1, 0.2, 0.3, 20, 'jakiś_tekst', False),  # String
            (-10.1, 0.2, 0.3, 20, 2.5, False),  # Negative number
            (10.1, -0.2, 0.3, 20, 0.1, False),  # Negative number
            (10.1, 0.2, -0.3, 20, 0.1, False),  # Negative number
            (10.1, 0.2, 0.3, -20, 0.1, False),  # Negative number
            (10.1, 0.2, 0.3, 20, -0.1, False),  # Negative number
    )
)
def test_stairs_form(X, Y, Z, V, W, validity):
    form = StairsForm(data={'X': X, 'Y': Y, 'Z': Z, 'V': V, 'W': W})
    assert form.is_valid() is validity


# Form - TypeValue
@pytest.mark.parametrize(
    'value, validity',
    (
            (7, True),  # Integer
            (7.6, True),  # Float
            ('jakiś_tekst', False),  # String
            (-7.6, False),  # Negative number
    )
)
def test_typevalue_form(value, validity):
    form = TypeValueForm(data={'value': value})
    assert form.is_valid() is validity


######################################################################################################################
######################################################################################################################


# Strona główna
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


# View - Rectangle
def test_rectangle_get(client):
    response = client.get('/calculate/rectangle/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_rectangle_post(client, add_shape):
    response = client.post(f'/concrete/{add_shape.pk}/', {'shape': 'Płyta_fund', 'volume': 9.5})
    assert response.status_code == 200
    print(response.content)

    form = RectangleForm(data={'X': 3.5, 'Y': 5.5, 'Z': 0.5})
    assert form.is_valid() is True
    form = RectangleForm(data={})
    assert form.is_valid() is False

    rectangle = List.objects.get(shape='shape_of_concrete')
    assert rectangle.volume == 12.3

    result = round((2.2 * 4.4 * 0.8), 1)
    assert result == 7.7


# View - Footing
def test_footing_get(client):
    response = client.get('/calculate/footing/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_footing_post(client, add_shape):
    response = client.post(f'/concrete/{add_shape.pk}/', {'shape': 'Ława fundamentowa', 'volume': 4.5})
    assert response.status_code == 200

    form = FootingForm(data={'X': 3.5, 'Y': 5.5, 'Z': 0.5, 'W': 0.2})
    assert form.is_valid() is True

    footing = List.objects.get(shape='shape_of_concrete')
    assert footing.volume == 12.3

    result = round(((10.9 * 8.8 * 2.1) - ((10.9 - 1.1 * 2) * (8.8 - 1.1 * 2) * 2.1)), 1)
    assert result == 80.9


# View - Cylinder
def test_cylinder_get(client):
    response = client.get('/calculate/cylinder/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_cylinder_post(client, add_shape):
    response = client.post(f'/concrete/{add_shape.pk}/', {'shape': 'Walec', 'volume': 54.8})
    assert response.status_code == 200

    form = CylinderForm(data={'Z': 3.5, 'R': 0.4})
    assert form.is_valid() is True

    cylinder = List.objects.get(shape='shape_of_concrete')
    assert cylinder.volume == 12.3

    result = round((pi * 0.4 * 0.4 * 3.5), 1)
    assert result == 1.8


# View - Triangle
def test_triangle_get(client):
    response = client.get('/calculate/triangle/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_triangle_post(client, add_shape):
    response = client.post(f'/concrete/{add_shape.pk}/', {'shape': 'Trójkąt', 'volume': 11.7})
    assert response.status_code == 200

    form = TriangleForm(data={'X': 3.5, 'Y': 5.5, 'Z': 0.5})
    assert form.is_valid() is True

    triangle = List.objects.get(shape='shape_of_concrete')
    assert triangle.volume == 12.3

    result = round(((3.5 * 5.5 * 0.5) * 0.5), 1)
    assert result == 4.8


# View - Slab
def test_slab_get(client):
    response = client.get('/calculate/slab/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_slab_post(client, add_shape):
    response = client.post(f'/concrete/{add_shape.pk}/', {'shape': 'Pływa z wgłębieniem', 'volume': 88.4})
    assert response.status_code == 200

    form = SlabForm(data={'X': 10.5, 'Y': 10.2, 'Z': 1.4, 'W': 2.1, 'H': 2.6})
    assert form.is_valid() is True

    slab = List.objects.get(shape='shape_of_concrete')
    assert slab.volume == 12.3

    result = round(((10.5 * 10.2 * 1.4) - (2.6 * 2.1 * 10.2)), 1)
    assert result == 94.2


# View - Stairs
def test_stairs_get(client):
    response = client.get('/calculate/stairs/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_stairs_post(client, add_shape):
    response = client.post(f'/concrete/{add_shape.pk}/', {'shape': 'Schody', 'volume': 74.3})
    assert response.status_code == 200

    form = StairsForm(data={'X': 10.3, 'Y': 0.15, 'Z': 0.3, 'W': 0.17, 'V': 15})
    assert form.is_valid() is True

    stairs = List.objects.get(shape='shape_of_concrete')
    assert stairs.volume == 12.3

    result = round(((10.5 * 10.2 * 1.4) - (2.6 * 2.1 * 10.2)), 1)
    assert result == 94.2


# View - TypeValue
def test_typevalue_get(client):
    response = client.get('/calculate/stairs/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_typevalue_post(client, add_shape):
    response = client.post(f'/concrete/{add_shape.pk}/', {'shape': 'Wpisz wartość', 'volume': 92.4})
    assert response.status_code == 200

    form = TypeValueForm(data={'value': 13.8})
    assert form.is_valid() is True

    stairs = List.objects.get(shape='shape_of_concrete')
    assert stairs.volume == 12.3

######################################################################################################################

# View - ConcreteView
@pytest.mark.django_db
def test_concrete(client, concreteview):
    response = client.post(f'/concrete/{concreteview.pk}/', {
                                             'concrete': 'C30/37',
                                             'use_of_concrete': 'Inne zastosowanie',
                                             'legal_name': 'Katarzyna Goździkowa',
                                             'phone': '505-607-459',
                                             'comment': 'Chocznia 123',
                                             'concrete_pomp': True,
                                             })
    assert response.status_code == 200
    l = List.objects.get(pk=concreteview.pk)
    assert l.concrete == 'C30/37'
    assert l.use_of_concrete == 'Inne zastosowanie'
    assert l.legal_name == 'Katarzyna Goździkowa'
    assert l.phone == '505-607-459'
    assert l.comment == 'Chocznia 123'
    assert l.concrete_pomp == True


# View - Summary
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

######################################################################################################################

# View - Contact (alfabetycznie)
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

######################################################################################################################

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

