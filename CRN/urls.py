
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

urlpatterns = [
	re_path(r'^select2/', include('django_select2.urls')),
    path('' , include('pages.urls')),
    re_path(r'', include('cr_note.urls')),
    re_path(r'^accounts/login/$' ,views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    re_path(r'^accounts/logged out/$' ,views.LogoutView.as_view(template_name="pages/index.html"),name='logout',kwargs={'next_page':'/'} ),

    path('admin/', admin.site.urls),
]
