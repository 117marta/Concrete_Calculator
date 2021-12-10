from calc.models import Concrete, Use, Person, Day
import pytest
from django.contrib.auth.models import User, Permission


# Dodanie nowego betonu do BD - OK (bez permission)
@pytest.fixture()
def add_concrete():
    return Concrete.objects.create(name='beton_super_mocny', description='opis_super_dlugi')


# @pytest.fixture()
# def show_person():
#     return Person.objects.create(
#         first_name="Imię",
#         last_name='Nazwisko',
#         description='Stanowisko',
#     )


# Osoby w CONTACT alfabetycznie
@pytest.fixture
def contact_four_person():
    return [
        Person.objects.create(first_name="Katarzyna", last_name='Broda', description='Sekretarka'),
        Person.objects.create(first_name="Zdzisław", last_name='Żuk', description='Majster'),
        Person.objects.create(first_name="Anna", last_name='Mańkut', description='Geodeta'),
        Person.objects.create(first_name="Dawid", last_name='Laskowski', description='Inżynier'),
    ]


# Dodawanie betonu do bazy z PERMISSION
@pytest.fixture
def user_with_permission():
    u = User.objects.create(username='test', password='pass')
    permission = Permission.objects.get(name='Can add concrete')
    u.user_permissions.add(permission)
    u = User.objects.get(username='test')
    return u


