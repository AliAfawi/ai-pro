from django.contrib import admin
from django.urls import path, include
from myapp import views as myapp_views
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', myapp_views.custom_login, name='login'),
    path('logout/', myapp_views.logout_user, name='logout'),  # Custom logout URL
    path('student_dashboard/', myapp_views.student_dashboard, name='student_dashboard'),
    path('practitioner_dashboard/', myapp_views.practitioner_dashboard, name='practitioner_dashboard'),
    # path('accounts/', include('django.contrib.auth.urls')),  # Includes all the authentication URLs
    path('student_register/', myapp_views.student_register, name='student_register'),
    path('practitioner_register/', myapp_views.practitioner_register, name='practitioner_register'),
    path('', myapp_views.home, name='home'),




        
    path('change-password/', views.CustomPasswordChangeView.as_view(), name='change_password'),

]


