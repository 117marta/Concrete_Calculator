from django.shortcuts import render, redirect
from django.views import View
from .forms import ShapeChoiceForm, RectangularForm, FootingForm, CylinderForm, TriangleForm, SlabForm, StairsForm, ConcreteForm, UseForm, LoginForm, RegisterForm
from .models import Use, Concrete, Person, Day, List
from math import pi, sqrt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.


#########################################################################################################################
class ShapeView(View):
    def get(self, request):
        form = ShapeChoiceForm()
        return render(request, 'calc/shape.html', {'form': form})


class ShapeChoiceView(View):
    def get(self, request):
        return render(request, 'calc/shape_choice.html')
    def post(self, request):
        X = float(request.POST.get('X'))
        Y = float(request.POST.get('Y'))
        Z = float(request.POST.get('Z'))
        # R = int(request.POST.get('R'))
        result = f'Objętość betonu: {round((X * Y * Z), 1)} m3'
        return render(request, 'calc/shape_choice.html', {'result': result})


#########################################################################################################################


class RectangularView(View):
    def get(self, request):
        form = RectangularForm()
        return render(request, 'calc/volume.html', {'form': form})
    def post(self, request):
        form = RectangularForm(request.POST)
        if form.is_valid():
            X = form.cleaned_data['X']
            Y = form.cleaned_data['Y']
            Z = form.cleaned_data['Z']
            result = round((X * Y * Z), 1)
            output = f'Objętość betonu: {result} m3'
            new_object = List.objects.create(shape='Płyta fundamentowa', volume=result)
            # get_id = f'Id twojego zamówienia na liście to: {new_object.pk}'
            # return render(request, 'calc/volume.html', {'form': form, 'output': output, 'get_id': get_id})
            return redirect(f'/concrete/{new_object.pk}')
        else:
            return render(request, 'calc/volume.html', {'form': form})


class FootingView(View):
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
            output = f'Objętość betonu: {result} m3'
            new_object = List.objects.create(shape='Ława fundamentowa', volume=result)
            # get_id = f'Id twojego zamówienia na liście to: {new_object.pk}'
            # return render(request, 'calc/volume.html', {'form': form, 'output': output, 'get_id': get_id})
            return redirect(f'/concrete/{new_object.pk}')
        else:
            return render(request, 'calc/volume.html', {'form': form})


class CylinderView(View):
    def get(self, request):
        form = CylinderForm()
        return render(request, 'calc/volume.html', {'form':  form})
    def post(self, request):
        form = CylinderForm(request.POST)
        if form.is_valid():
            Z = float(form.cleaned_data['Z'])
            R = float(form.cleaned_data['R'])
            result = round((pi * R * R * Z), 1)
            output = f'Objętość betonu: {result} m3'
            new_object = List.objects.create(shape='Walec', volume=result)
            get_id = f'Id twojego zamówienia na liście to: {new_object.pk}'
            # get_id = 100
            # return render(request, 'calc/volume.html', {'form': form, 'output': output, 'get_id': get_id})
            return redirect(f'/concrete/{new_object.pk}', get_id=get_id)
        else:
            return render(request, 'calc/volume.html', {'form', form})


class TriangleView(View):
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
            output = f'Objętość betonu: {result} m3'
            new_object = List.objects.create(shape='Trójkąt', volume=result)
            # get_id = f'Id twojego zamówienia na liście to: {new_object.pk}'
            # return render(request, 'calc/volume.html', {'form': form, 'output': output, 'get_id': get_id})
            return redirect(f'/concrete/{new_object.pk}')
        else:
            return render(request, 'calc/volume.html', {'form': form})


class SlabView(View):
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
            output = f'Objętość betonu: {result} m3'
            new_object = List.objects.create(shape='Płyta z wgłębieniem', volume=result)
            # get_id = f'Id twojego zamówienia na liście to: {new_object.pk}'
            # return render(request, 'calc/volume.html', {'form': form, 'output': output, 'get_id': get_id})
            return redirect(f'/concrete/{new_object.pk}')
        else:
            return render(request, 'calc/volume.html', {'form': form})


class StairsView(View):
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
            output = f'Objętość betonu: {result} m3'
            new_object = List.objects.create(shape='Schody', volume=result)
            # get_id = f'Id twojego zamówienia na liście to: {new_object.pk}'
            # return render(request, 'calc/volume.html', {'form': form, 'output': output, 'get_id': get_id})
            return redirect(f'/concrete/{new_object.pk}')
        else:
            return render(request, 'calc/volume.html', {'form': form})


class ConcreteView(View):
    """Allows to choose the type of concrete and its uses."""
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
            form_comment = form.cleaned_data['form_comment']
            add_data = List.objects.get(pk=id)
            add_data.concrete = form_concrete.name
            add_data.use_of_concrete = form_use.name
            add_data.legal_name = form_legal_name
            add_data.comment = form_comment
            add_data.save()
            # result = f'ID zastosowania: {form_use.id} // \n ID betonu: {form_concrete.id}'
            return redirect(f'/summary/{add_data.pk}')
        else:
            return render(request, 'calc/concrete.html', {'form': form})



# DOBRE - PRZED ZMIANAMI Z URL I id W ADRESIE
# class ConcreteView(View):
#     """Allows to choose the type of concrete and its uses."""
#     def get(self, request):
#         form = ConcreteForm(initial={'form_use': 5, 'form_concrete': 3})
#         return render(request, 'calc/concrete.html', {'form': form})
#     def post(self, request):
#         form = ConcreteForm(request.POST)
#         if form.is_valid():
#             form_use = form.cleaned_data['form_use']
#             # use_id = Concrete.objects.filter(id=form_use.id)
#             form_concrete = form.cleaned_data['form_concrete']
#             # concrete = Concrete.objects.filter(id=form_concrete.id)
#             # List.objects.create()
#             result = f'ID zastosowania: {form_use.id} // \n ID betonu: {form_concrete.id}'
#             return render(request, 'calc/concrete.html', {'form': form, 'result': result})
#         else:
#             return render(request, 'calc/concrete.html', {'form': form})


class SummaryView(View):
    def get(self, request, id):
        summary = List.objects.get(pk=id)
        return render(request, 'calc/summary.html', {'summary': summary})






# class ConcreteView(View):
#     def get(self, request):
#         form = ConcreteForm
#         return render(request, 'calc/concrete.html', {'form': form})
#     def post(self, request):
#         form = ConcreteForm(request.POST)
#         if form.is_valid():
#             form_use = form.cleaned_data['form_use']
#             form_select = Concrete.objects.filter(id=form_use.id)
#             form_concrete = form.cleaned_data['form_concrete']
#             result = f'ID zastosowania: {form_use.id}'
#             return render(request, 'calc/concrete.html', {'form': form, 'result': result})
#         else:
#             return render(request, 'calc/concrete.html', {'form': form})




class ContactView(View):
    """Displays when employees can be contacted."""
    def get(self, request):
        persons_in_work = Person.objects.all().order_by('first_name', 'last_name')
        days_of_work = Day.objects.all().order_by('day', 'hour')
        return render(request, 'calc/contact.html', {'persons_in_work': persons_in_work, 'days_of_work': days_of_work})
    def post(self, request):
        pass


class ListUsersView(View):
    def get(self, request):
        users = Person.objects.all()


class LoginView(View):
    """Allows to log in a user."""
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
    """Allows to log out a user."""
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterView(View):
    """Allows to register a new user."""
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


# przechodzi testy, ale bez 'permission'
class AddConcreteView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
# class AddConcreteView(SuccessMessageMixin, CreateView):
    """Add new concrete to the database - only by an authorizated user."""
    permission_required = 'calc.add_concrete'
    model = Concrete
    fields = '__all__'
    success_message = 'Dodano beton <b> %(name)s </b> do bazy!'
    success_url = '/add_concrete/'


# class AddConcreteView2(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
#     """Add new concrete to database."""
#     permission_required = 'calc.add_concrete'
#     model = Concrete
#     fields = '__all__'
#     success_message = 'Dodano beton <b> %(name)s </b> do bazy!'
#     success_url = '/add_concrete/'



# To co chcę na sam koniec zrobić
# class ListView(SuccessMessageMixin, CreateView):
#     model = List
#     fields = '__all__'
#     success_message = 'Oto podsumowanie twojego zamówienia'
#     success_url = '/list/'

