from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('printpagecall/',views.printpagecall, name='printpagecall'),
    path('printpagelogic/',views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),



    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),






    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserLoginPageCall/',views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
    path('calculatorpagecall/', views.calculatorpagecall, name='calculatorpagecall'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('datetimepagecall/',views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/',views.datetimepagelogic, name='datetimepagelogic'),
    path('timezonepagecall/',views.timezonepagecall, name='timezonepagecall'),
    path('timezonepagelogic/', views.timezonepagelogic, name='timezonepagelogic'),
    path('add/', views.add_student, name='add_student'),
    path('list/', views.student_list, name='student_list'),

    path('upload_file/', views.upload_file, name='upload_file'),
    path('cards/', views.cards, name='cards'),

    path('add_contact/', views.add_contact, name='add_contact'),
    path('contact_list', views.contact_list, name='contact_list'),
    path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('email_contact/<int:pk>/', views.email_contact, name='email_contact'),


]
