"""
URL configuration for MiniProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from user import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stockit/',include('StockIt.urls')),
    path('reg/',user_view.reg,name="u_reg"),
    path('',auth_views.LoginView.as_view(template_name='user/login.html'),name='u_lin'),
    path('profile/',user_view.profile, name='user-profile'),
    path('profile/update/', user_view.profile_update,name='user-profile-update'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='u_lout'),
    path('pwd_reset/', auth_views.PasswordResetView.as_view(),name='p_rst'),
    path('pwd_rst_done/',auth_views.PasswordResetDoneView.as_view(),name='p_rst_done'),
    path('pwd_rst_cfm/',auth_views.PasswordResetConfirmView.as_view(),name='p_rst_cfm'),

]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
