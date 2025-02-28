from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import by_rubric
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('table/', views.table, name='table'),
    path('tank_table/', views.tank_table, name='tank_table'),
    path('form/', views.form, name='form'),
    path('login_page/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('add-product/', views.add_product, name='add_product'),
    path('<int:student_id>/', views.student_courses, name='student_courses'),
    path('<int:course_id>/', views.course_students, name='course_students'),
    path('rubric/<int:rubric_id>/', by_rubric, name='by_rubric'),
    # path('', views.HomePageView.as_view(), name='index2'),
    # path('about/', views.AboutPageView.as_view(), name='about2'),
    path('data/', views.DataPageView.as_view(), name='data'),
]


urlpatterns += staticfiles_urlpatterns()
