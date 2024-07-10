from django.contrib import admin
from django.urls import path
from myapp.views import custom_login, student_register, practitioner_register, home, student_dashboard, practitioner_dashboard, logout_user, CustomPasswordChangeView, PasswordResetRequestView, CodeVerificationView
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404
from django.urls import path, include
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', custom_login, name='login'),
    path('student_register/', student_register, name='student_register'),
    path('practitioner_register/', practitioner_register, name='practitioner_register'),
    path('', home, name='home'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('practitioner_dashboard/', practitioner_dashboard, name='practitioner_dashboard'),
    path('logout/', logout_user, name='logout'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('password_reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('verify_code/', CodeVerificationView.as_view(), name='verify_code'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('', include('myapp.urls')),  # include your app's urls here
]


handler404 = custom_404