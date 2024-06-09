from django.contrib import admin
from django.urls import path, include
from home import views
from home.views import about
# Django admin header customization

admin.site.site_header="The Wayanad Voyage"
admin.site.site_title="Welcome to The Trip, Wayanad-Dashboard"
admin.site.index_title="Welcome to this portal!"
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('rooms', views.rooms, name='rooms'),
    path('about/', about, name='about'),
    path('contact', views.contact, name='contact'),
    path('registerPage', views.registerPage, name='registerPage'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('logout', views.logoutUser, name='logout'),
    path('booking', views.booking, name='booking'),
    path('emp', views.emp, name='emp'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('empsign', views.empsign, name='empsign'),
]
