"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calc.views import ShapeChoiceView, ShapeView, RectangularView, FootingView, CylinderView, \
    TriangleView, SlabView, StairsView, ConcreteView, ContactView, \
    LoginView, LogoutView, RegisterView, AddConcreteView, SummaryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ShapeChoiceView.as_view()),
    path('shape/', ShapeView.as_view()),
    path('calculate/rectangle/', RectangularView.as_view()),
    path('calculate/footing/', FootingView.as_view()),
    path('calculate/cylinder/', CylinderView.as_view()),
    path('calculate/triangle/', TriangleView.as_view()),
    path('calculate/slab/', SlabView.as_view()),
    path('calculate/stairs/', StairsView.as_view()),
    # path('concrete/', ConcreteView.as_view()),
    path('contact/', ContactView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('add_concrete/', AddConcreteView.as_view(), name='add-concrete'),
    path('concrete/<int:id>', ConcreteView.as_view()),
    path('summary/<int:id>', SummaryView.as_view()),
]
