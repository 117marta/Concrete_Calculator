from django.shortcuts import render, redirect
from django.views import View
from .forms import RectangleForm, FootingForm, CylinderForm, TriangleForm, SlabForm, StairsForm, TypeValueForm, \
    ConcreteForm, LoginForm, RegisterForm
from .models import Use, Concrete, Person, Day, List
from math import pi, sqrt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

# Create your views here.


class RectangleView(View):
    """
    Display a rectangle form, in which you can calculate rectangle-shape volume by filling its form fields.
    Create a new object in List database.

    allowed methods: GET, POST.
    template: volume.html
    :param request:
    :return: Redirect to concrete page by Primary Key (pk) in List database.
    """
    def get(self, request):
        form = RectangleForm()
        return render(request, 'calc/volume.html', {'form': form})
    def post(self, request):
        form = RectangleForm(request.POST)
        if form.is_valid():
            X = form.cleaned_data['X']
            Y = form.cleaned_data['Y']
            Z = form.cleaned_data['Z']
            result = round((X * Y * Z), 1)
            new_object = List.objects.create(shape='Płyta fundamentowa', volume=result)
            return redirect(f'/concrete/{new_object.pk}')
        else:
            return render(request, 'calc/volume.html', {'form': form})


class FootingView(View):
    """
    Display a footing form, in which you can calculate footing-shape volume by filling its form fields.
    Create a new object in List database.

    allowed methods: GET, POST.
    template: volume.html
    :param request:
    :return: Redirect to concrete page by Primary Key (pk) in List database.
    """
    def get(self, request):
        form = FootingForm()
        return render(request, 'calc/volume.html', {'form': form})
    def post(self, request):
        form = FootingForm(request.POST)
        if form.is_valid():
            X = form.cleaned_data['X']
            Y = form.cleaned_data['Y']
            Z = form.cleaned_data['Z']
            W = form.cleaned_data['W']
            result = round(((X * Y * Z) - ((X - W * 2) * (Y - W * 2) * Z)), 1)
            new_object = List.objects.create(shape='Ława fundamentowa', volume=result)
            return redirect(f'/concrete/{new_object.pk}')
        else:
            return render(request, 'calc/volume.html', {'form': form})


class CylinderView(View):
    """
    Display a cylinder form, in which you can calculate cylinder-shape volume by filling its form fields.
    Create a new object in List database.

    allowed methods: GET, POST.
    template: volume.html
    :param request:
    :return: Redirect to concrete page by Primary Key (pk) in List database.
    """
    def get(self, request):
        form = CylinderForm()
        return render(request, 'calc/volume.html', {'form':  form})
    def post(self, request):
        form = CylinderForm(request.POST)
        if form.is_valid():
            Z = float(form.cleaned_data['Z'])
            R = float(form.cleaned_data['R'])
            result = round((pi * R * R * Z), 1)
            new_object = List.objects.create(shape='Walec', volume=result)
            get_id = f'Id twojego zamówienia na liście to: {new_object.pk}'
            return redirect(f'/concrete/{new_object.pk}', get_id=get_id)
        else:
            return render(request, 'calc/volume.html', {'form', form})


class TriangleView(View):
    """
    Display a triangle form, in which you can calculate triangle-shape volume by filling its form fields.
    Create a new object in List database.

    allowed methods: GET, POST.
    template: volume.html
    :param request:
    :return: Redirect to concrete page by Primary Key (pk) in List database.
    """
    def get(self, request):
        form = TriangleForm()
        return render(request, 'calc/volume.html', {'form': form})
    def post(self, request):
        form = TriangleForm(request.POST)
        if form.is_valid():
            X = form.cleaned_data['X']
            Y = form.cleaned_data['Y']
            Z = form.cleaned_data['Z']
            result = round(((X * Y * Z) * 0.5), 1)
            new_object = List.objects.create(shape='Trójkąt', volume=result)
            return redirect(f'/concrete/{new_object.pk}')
        else:
            return render(request, 'calc/volume.html', {'form': form})


class SlabView(View):
    """
    Display a slab form, in which you can calculate slab-shape volume by filling its form fields.
    Create a new object in List database.

    allowed methods: GET, POST.
    template: volume.html
    :param request:
    :return: Redirect to concrete page by Primary Key (pk) in List database.
    """
    def get(self, request):
        form = SlabForm()
        return render(request, 'calc/volume.html', {'form': form})
    def post(self, request):
        form = SlabForm(request.POST)
        if form.is_valid():
            X = form.cleaned_data['X']
            Y = form.cleaned_data['Y']
            Z = form.cleaned_data['Z']
            W = form.cleaned_data['W']
            H = form.cleaned_data['H']
            result = round(((X * Y * Z) - (H * W * Y)), 1)
            new_object = List.objects.create(shape='Płyta z wgłębieniem', volume=result)
            return redirect(f'/concrete/{new_object.pk}')
        else:
            return render(request, 'calc/volume.html', {'form': form})


class StairsView(View):
    """
    Display a stairs form, in which you can calculate stairs-shape volume by filling its form fields.
    Create a new object in List database.

    allowed methods: GET, POST.
    template: volume.html
    :param request:
    :return: Redirect to concrete page by Primary Key (pk) in List database.
    """
    def get(self, request):
        form = StairsForm()
        return render(request, 'calc/volume.html', {'form': form})
    def post(self, request):
        form = StairsForm(request.POST)
        if form.is_valid():
            X = form.cleaned_data['X']
            Y = form.cleaned_data['Y']
            Z = form.cleaned_data['Z']
            W = form.cleaned_data['W']
            V = form.cleaned_data['V']
            result = round(((X * Y * Z * 0.5) * V + (W * X * sqrt(Y * Y + Z * Z)) * V), 1)
            new_object = List.objects.create(shape='Schody', volume=result)
            return redirect(f'/concrete/{new_object.pk}')
        else:
            return render(request, 'calc/volume.html', {'form': form})


class TypeValue(View):
    """
    Display a form, in which you can enter any value.
    Create a new object in List database.

    allowed methods: GET, POST.
    template: volume.html
    :param request:
    :return: Redirect to concrete page by Primary Key (pk) in List database.
    """
    def get(self, request):
        form = TypeValueForm()
        return render(request, 'calc/volume.html', {'form': form})
    def post(self, request):
        form = TypeValueForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data['value']
            new_object = List.objects.create(shape='-', volume=result)
            return redirect(f'/concrete/{new_object.id}')
        else:
            return render(request, 'calc/volume.html', {'form': form})


class ConcreteView(View):
    """
    Allow to choose the type of concrete and its uses; enter legal name, phone, comment and choose if you want to order
    a conrete pomp.

    allowed methods: GET, POST.
    template: concrete.html
    :param request:
    :param int id: Primary Key (pk) in List database.
    :return: Redirect to summary page.
    """
    def get(self, request, id):
        form = ConcreteForm(initial={'form_use': 5, 'form_concrete': 3})
        get_id = List.objects.get(pk=id)
        return render(request, 'calc/concrete.html', {'form': form, 'get_id': get_id})
    def post(self, request, id):
        form = ConcreteForm(request.POST)
        if form.is_valid():
            form_use = form.cleaned_data['form_use']
            form_concrete = form.cleaned_data['form_concrete']
            form_legal_name = form.cleaned_data['form_legal_name']
            form_phone = form.cleaned_data['form_phone']
            form_concrete_pomp = form.cleaned_data['form_concrete_pomp']
            form_comment = form.cleaned_data['form_comment']
            add_data = List.objects.get(pk=id)
            add_data.concrete = form_concrete.name
            add_data.use_of_concrete = form_use.name
            add_data.legal_name = form_legal_name
            add_data.phone = form_phone
            add_data.concrete_pomp = form_concrete_pomp
            add_data.comment = form_comment
            add_data.save()
            return redirect(f'/summary/{add_data.pk}')
        else:
            return render(request, 'calc/concrete.html', {'form': form})


class SummaryView(View):
    """
    Display summary of client's order.

    allowed methods: GET.
    template: summary.html
    :param request:
    :return: The Request response - summary page.
    """
    def get(self, request, id):
        summary = List.objects.get(pk=id)
        return render(request, 'calc/summary.html', {'summary': summary})


class ContactView(View):
    """
    Display when employees can be contacted.

    allowed methods: GET.
    template: contact.html
    :param request:
    :return: The Request response - employees contact page.
    """
    def get(self, request):
        persons_in_work = Person.objects.all().order_by('first_name', 'last_name')
        days_of_work = Day.objects.all().order_by('day', 'hour')
        return render(request, 'calc/contact.html', {'persons_in_work': persons_in_work, 'days_of_work': days_of_work})


class LoginView(View):
    """
    Allow to log in a user.

    allowed methods: GET, POST.
    template: login.html
    :param request:
    :return: Redirect to main page.
    """
    def get(self, request):
        form = LoginForm()
        return render(request, 'calc/login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'calc/login.html', {'form': form, 'message': 'Błędny login lub hasło!'})


class LogoutView(View):
    """
    Allow to log out a user.

    allowed methods: GET.
    :param request:
    :return: Redirect to main page.
    """
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterView(View):
    """
    Allow to register a new user.

    allowed methods: GET, POST.
    template: register.html
    :param request:
    :return: The Request response.
    """
    def get(self, request):
        form = RegisterForm()
        return render(request, 'calc/register.html', {'form': form})
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            name = form.cleaned_data['first_name']
            surname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            User.objects.create_user(username=login, email=email, password=password, first_name=name, last_name=surname)
            message = 'Stworzono użytkownika!'
            return render(request, 'calc/register.html', {'form': form, 'message': message})
        else:
            return render(request, 'calc/register.html', {'form': form})


class AddConcreteView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Add new concrete to the database - only by an authorizated user.

    allowed methods: GET, POST.
    template: concrete_form.html
    :param request:
    :return: The Request response.
    """
    permission_required = 'calc.add_concrete'
    model = Concrete
    fields = '__all__'
    success_message = 'Dodano beton <b> %(name)s </b> do bazy!'
    success_url = '/add_concrete/'

