from django.urls import path

from .view.register import register,verify_otp
from .view.login import student_login
from .view.dashboard import dashboard
from .view.logout import logout
from .view.homepage import homepage
from .view.about import about
from .view.footer import footer
from .view.delete import delete
from .view.contact import contact
from .view.admin_login import admin_login
from .view.thank_you import thank_you
from .view.admin_dashboard import admin_dashboard
from .view.your_data import your_data

from .view.feedback import feedback
from .view.feedback_delete import feedback_delete,contact_delete


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', student_login, name='login'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/', logout, name='logout'),
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('footer/', footer, name='footer'),
    path('contact/', contact, name='contact'),
    path('admin_login/', admin_login, name='admin_login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('delete/<int:id>/',delete, name='delete'),
    path('feedback/', feedback, name='feedback'),
    path('thank_you/', thank_you, name='thank_you'),
    path('feedback_delete/<int:id>/', feedback_delete, name='feedback_delete'),
    path('contact_delete/<int:id>/', contact_delete, name='contact_delete'),

    path('your_data/', your_data, name='your_data'),




]
