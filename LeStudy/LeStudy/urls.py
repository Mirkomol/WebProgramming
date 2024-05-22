
from django.contrib import admin
from django.urls import path
from LetsStudyApp import views
from django.conf import settings
from django.conf.urls.static import static
from LetsStudyApp.views import StudentDetailView, homeView, libraryView
from django.contrib.auth import views as authentication_views

urlpatterns = [
                  path('iamsuperadmin', admin.site.urls),

                  path('', homeView.as_view(), name='home'),

                  path('game', views.game, name='game'),

                  path('library', libraryView.as_view(), name='library'),

                  path('add_book', views.addBook, name='add_book'),

                  path('add_student', views.add_student, name='add_student'),

                  path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),

                  path('login/', views.user_login, name='login'),

                  path('register/', views.register, name='register'),

                  path('logout/', authentication_views.LogoutView.as_view(template_name='LetsStudyApp/logout.html'),
                       name='logout'),

               ] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)