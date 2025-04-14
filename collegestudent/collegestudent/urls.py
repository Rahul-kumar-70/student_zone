"""
URL configuration for collegestudent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from testapp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('thank/',views.thanks,name='thank'),
    path('index/',views.indexpage),
    path('about/',views.aboutpage),
    path('signup/',views.signuppage),
    path('list/', views.StudentList.as_view()),
    path('<int:pk>', views.StudentDetail.as_view(),name='studentdetail'),
    path('form/', views.StudentForm.as_view()),
    path('update/<int:pk>', views.StudentUpdate.as_view()),
    path('delete/<int:pk>', views.StudentDelete.as_view()),
    path('listphd/', views.StudentPhdList.as_view()),
    path('phd/<int:pk>', views.StudentPhddetail.as_view()),
    path('formphd/', views.StudentPhdform.as_view()),
    path('updatephd/<int:pk>', views.StudentPhdUpdate.as_view()),
    path('deletephd/<int:pk>', views.StudentPhdDelete.as_view()),
    path('inquery/', views.StudentEnq.as_view()),
     path('logout/',views.logoutpage),
    path('accounts/',include('django.contrib.auth.urls')),
    path('search/', views.search_marksheet, name='search_marksheet'),
    path('mlist/', views.MarksheetList.as_view()),
    path('mdetail/<int:pk>', views.MarksheetDetail.as_view(),name='detail'),
    path('mform/', views.MarksheetForm.as_view()),
    path('mdelete/<int:pk>', views.MarksheetDelete.as_view()),
    path('mupdate/<int:pk>', views.MarksheetUpadate.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
