from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from MainApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    #path('services/',views.Services,name='services'),
    path('plans/',views.plans,name='plans'),
    path('contact/',views.contact,name='contacts'),
    #path('news/',views.News,name='news'),
    path('binary/<int:p>/<int:c>/',views.binary),
    path('feedback/',views.feedback),
    path('member/',views.member),
    path('register/<int:pid>/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('profile/',views.profile),
    path('adminProfile/',views.adminProfile),
    path('updateall/',views.updateAll),
    path('updateprofile/<int:num>',views.updateProfile),
    path('bankdetails/<int:num>',views.updateBankDetails),
    path('deactivate/',views.deactivateAccount),
    path('reset/',views.resetAll),
    path('activate/<int:num>/',views.activate),
]
urlpatterns=urlpatterns+staticfiles_urlpatterns()
urlpatterns=urlpatterns+static(settings.MEDIA_URL,
                               document_root=settings.MEDIA_ROOT)