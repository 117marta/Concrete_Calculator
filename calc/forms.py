from django import forms
from .models import Concrete, Use, List
from django.contrib.auth.models import User
from django.core.validators import URLValidator, validate_email, ValidationError


# class ShapeChoiceForm(forms.Form):
#     """Chooses a shape of concrete."""
#     SHAPES = (
#         ('rectangular', 'Płyta fundamentowa'),
#         ('footing', 'Ława fundamentowa'),
#         ('cylinder', 'Walec'),
#         ('triangle', 'Trójąt'),
#         ('slab', 'Płyta z wgłębieniem'),
#         ('stairs', 'Schody'),
#     )
#     shapes = forms.MultipleChoiceField(choices=SHAPES, label='Wybór kształtu', widget=forms.RadioSelect)
#


# FIGURY
class RectangularForm(forms.Form):  # Płyta fundamentowa
    X = forms.FloatField(label='X:', widget=forms.TextInput(attrs={'placeholder': 'Długość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    Y = forms.FloatField(label='Y:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})


class FootingForm(forms.Form):   # Ława fundamentowa
    X = forms.FloatField(label='X:', widget=forms.TextInput(attrs={'placeholder': 'Długość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    Y = forms.FloatField(label='Y:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    W = forms.FloatField(label='W:', widget=forms.TextInput(attrs={'placeholder': 'Głębokość ławy [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})


class CylinderForm(forms.Form):  # Walec
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    R = forms.FloatField(label='H:', widget=forms.TextInput(attrs={'placeholder': 'Promień [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})


class TriangleForm(forms.Form):  # Trójkąt
    X = forms.FloatField(label='X:', widget=forms.TextInput(attrs={'placeholder': 'Długość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    Y = forms.FloatField(label='Y:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})


class SlabForm(forms.Form):  # Płyta z wgłębieniem
    X = forms.FloatField(label='X:', widget=forms.TextInput(attrs={'placeholder': 'Długość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    Y = forms.FloatField(label='Y:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    W = forms.FloatField(label='W:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość wgłębienia [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    H = forms.FloatField(label='H:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość wgłębienia [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})


class StairsForm(forms.Form):  # Schody
    X = forms.FloatField(label='X:', widget=forms.TextInput(attrs={'placeholder': 'Długość schodka [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    Y = forms.FloatField(label='Y:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość schodka [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość schodka [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    V = forms.FloatField(label='V:', widget=forms.TextInput(attrs={'placeholder': 'Liczba stopni'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})
    W = forms.FloatField(label='W:', widget=forms.TextInput(attrs={'placeholder': 'Grubość płyty pod schodami [m]'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})


class TypeValueForm(forms.Form):
    value = forms.FloatField(label='Podaj wartość:', widget=forms.TextInput(attrs={'placeholder': 'Wpisz objętość'}), min_value=0, error_messages={'min_value': 'Wpisz liczbę dodatnią!'})


# ZAMÓWIENIE
class ConcreteForm(forms.Form):
    form_use = forms.ModelChoiceField(queryset=Use.objects.all(), label='Zastosowanie')
    form_concrete = forms.ModelChoiceField(queryset=Concrete.objects.all(), label='Beton')
    form_legal_name = forms.CharField(max_length=150, label='Imię i Nazwisko')
    form_phone = forms.IntegerField(label='Telefon')
    form_concrete_pomp = forms.BooleanField(label='Pompa do betonu', required=False)
    form_comment = forms.CharField(widget=forms.Textarea, label='Komentarz do zamówienia')
    # form_concrete_pomp = forms.BooleanField(label='Pompa do betonu', widget=forms.RadioSelect(choices=((False, 'NIE'), (True, 'TAK'))))


# class ConcreteForm2222222222222(forms.ModelForm):
#     form_use = forms.ModelChoiceField(queryset=Use.objects.all(), label='Zastosowanie')
#     form_concrete = forms.ModelChoiceField(queryset=Concrete.objects.all(), label='Beton')
#     class Meta:
#         model = List
#         fields = ['form_use', 'form_concrete', 'legal_name', 'comment', 'phone', 'concrete_pomp', 'created_date']





# LOGOWANIE I REJESTRACJA
class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


def login_not_taken(login):
    if User.objects.filter(username=login):
        raise ValidationError('Podany login jest zajęty.')

class RegisterForm(forms.Form):
    login = forms.CharField(label='Login', validators=[login_not_taken])
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    email = forms.EmailField(label='E-mail')

    def clean(self):
        """
        Validate the given value and return its "cleaned" value as an
        appropriate Python object. Raise ValidationError for any errors.
        """
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise ValidationError('Hasła nie są takie same!')
        return cleaned_data


