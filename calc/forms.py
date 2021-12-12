from django import forms
from .models import Concrete, Use
from django.forms import CheckboxSelectMultiple, CheckboxInput
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.validators import URLValidator, validate_email, ValidationError


class ShapeChoiceForm(forms.Form):
    """Chooses a shape of concrete."""
    SHAPES = (
        ('rectangular', 'Płyta fundamentowa'),
        ('footing', 'Ława fundamentowa'),
        ('cylinder', 'Walec'),
        ('triangle', 'Trójąt'),
        ('slab', 'Płyta z wgłębieniem'),
        ('stairs', 'Schody'),
    )
    shapes = forms.MultipleChoiceField(choices=SHAPES, label='Wybór kształtu', widget=forms.RadioSelect)




# class ShapeForm(forms.Form):
#     X = forms.FloatField(label='Długość:')
#     Y = forms.FloatField(label='Szerokość:')
#     Z = forms.FloatField(label='Wysokość:')
#     R = forms.FloatField(label='Promień:')
#     W = forms.FloatField(label='Szerokość wgłębienia:')
#     H = forms.FloatField(label='Wysokość wgłębienia:')
#     V = forms.FloatField(label='Liczba schodków:')
#     T = forms.FloatField(label='Długość płyty:')
#     value = forms.FloatField(label='Podaj wartość:')


class RectangularForm(forms.Form):  # Płyta fundamentowa
    X = forms.FloatField(label='X:', widget=forms.TextInput(attrs={'placeholder': 'Długość [m]'}))
    Y = forms.FloatField(label='Y:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość [m]'}))
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość [m]'}))


class FootingForm(forms.Form):   # Ława fundamentowa
    X = forms.FloatField(label='X:', widget=forms.TextInput(attrs={'placeholder': 'Długość [m]'}))
    Y = forms.FloatField(label='Y:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość [m]'}))
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość [m]'}))
    W = forms.FloatField(label='W:', widget=forms.TextInput(attrs={'placeholder': 'Głębokość ławy [m]'}))


class CylinderForm(forms.Form):  # Walec
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość [m]'}))
    R = forms.FloatField(label='H:', widget=forms.TextInput(attrs={'placeholder': 'Promień [m]'}))


class TriangleForm(forms.Form):  # Trójkąt
    X = forms.FloatField(label='X:', widget=forms.TextInput(attrs={'placeholder': 'Długość [m]'}))
    Y = forms.FloatField(label='Y:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość [m]'}))
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość [m]'}))


class SlabForm(forms.Form):  # Płyta z wgłębieniem
    X = forms.FloatField(label='X:', widget=forms.TextInput(attrs={'placeholder': 'Długość [m]'}))
    Y = forms.FloatField(label='Y:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość [m]'}))
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość [m]'}))
    W = forms.FloatField(label='W:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość wgłębienia [m]'}))
    H = forms.FloatField(label='H:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość wgłębienia [m]'}))


class StairsForm(forms.Form):  # Schody
    X = forms.FloatField(label='X:', widget=forms.TextInput(attrs={'placeholder': 'Długość schodka [m]'}))
    Y = forms.FloatField(label='Y:', widget=forms.TextInput(attrs={'placeholder': 'Szerokość schodka [m]'}))
    Z = forms.FloatField(label='Z:', widget=forms.TextInput(attrs={'placeholder': 'Wysokość schodka [m]'}))
    V = forms.FloatField(label='V:', widget=forms.TextInput(attrs={'placeholder': 'Liczba stopni'}))
    W = forms.FloatField(label='W:', widget=forms.TextInput(attrs={'placeholder': 'Grubość płyty pod schodami [m]'}))


class TypeValueForm(forms.Form):
    value = forms.FloatField(label='Podaj wartość:', widget=forms.TextInput(attrs={'placeholder': 'Wpisz objętość'}))



# class ConcreteForm(forms.ModelForm):
    # class Meta:
    #     model = Concrete
    #     fields = '__all__'
    #     # widgets = {'is_anything_required' : CheckboxInput(attrs={'class': 'required checkbox form-control'})}
    #     widgets = {'labels': forms.MultipleChoiceField()}


# class ConcreteForm(forms.Form):
#     form_use = forms.ModelChoiceField(queryset=Use.objects.all(), label='Zastosowanie')
#     form_concrete = forms.ModelChoiceField(queryset=Concrete.objects.all(), label='Beton', required=False)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['form_concrete'].queryset = Use.objects.none()
#
#         self.fields['form_concrete'].queryset = Use.objects.filter(id=6)
#
#         if 'form_use' in self.data:
#             try:
#                 use_id = int(self.data.get('form_use'))
#                 self.fields['form_concrete'].queryset = Concrete.objects.filter(id=use_id)
#             except (ValueError, TypeError):
#                 pass
#         elif self.instance.pk:
#             self.fields['form_concrete'].queryset = self.instance.use_conc_set






class ConcreteForm(forms.Form):
    form_use = forms.ModelChoiceField(queryset=Use.objects.all(), label='Zastosowanie')
    form_concrete = forms.ModelChoiceField(queryset=Concrete.objects.all(), label='Beton')
    form_legal_name = forms.CharField(max_length=150, label='Imię i Nazwisko')
    form_phone = forms.IntegerField(label='Telefon')
    form_comment = forms.CharField(widget=forms.Textarea, label='Komentarz do zamówienia')




class UseForm(forms.ModelForm):
    class Meta:
        model = Use
        fields = '__all__'


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
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise ValidationError('Hasła nie są takie same!')
        return cleaned_data


