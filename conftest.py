from calc.models import Concrete, Use, Person, Day, List
import pytest
from django.contrib.auth.models import User, Permission


# View - Rectangle, Footing, Cylinder, Triangle, Slab, Stairs, TypeValue
@pytest.fixture()
def add_shape():
    return List.objects.create(
        shape='shape_of_concrete',
        volume=12.3,
    )


# @pytest.fixture()
# def rectangle_result():
#     X = 12.2
#     Y = 14.4
#     Z = 1.8
#     result = round((X * Y * Z), 1)
#     return result



# View - ConcreteView
@pytest.fixture
def concreteview():
    return List.objects.create(
        concrete='C30/37',
        use_of_concrete='Inne zastosowanie',
        legal_name='Katarzyna Goździkowa',
        phone='505-607-459',
        comment='Chocznia 123',
        concrete_pomp=True,
    )


# View - Summary
@pytest.fixture
def summary_show():
    return List.objects.create(
        shape='Kształt',
        volume=1234,
        concrete='C30/37',
        use_of_concrete='Fundamenty',
        comment='Kozia Wólka 521',
        legal_name='Kamil Chrzanowski',
        phone='500600700',
        concrete_pomp=True,
    )


# View - Contact (alfabetycznie)
@pytest.fixture
def contact_four_persons():
    return [
        Person.objects.create(first_name="Katarzyna", last_name='Broda', description='Sekretarka'),
        Person.objects.create(first_name="Zdzisław", last_name='Żuk', description='Majster'),
        Person.objects.create(first_name="Anna", last_name='Mańkut', description='Geodeta'),
        Person.objects.create(first_name="Dawid", last_name='Laskowski', description='Inżynier'),
    ]


# Dodawanie betonu do bazy z permission "calc.add_concrete"
@pytest.fixture
def user_with_permission():
    u = User.objects.create(username='test', password='pass')
    permission = Permission.objects.get(name='Can add concrete')
    u.user_permissions.add(permission)
    u = User.objects.get(username='test')
    return u
