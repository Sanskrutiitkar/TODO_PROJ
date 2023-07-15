
from django.contrib import admin
from django.urls import path
from todoapp.views import home,usignup,todo,ulogout,uchangepass,about,todocreate, tododelete,todoview,todocomp

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home , name="home"),
    path("usignup/" , usignup , name="usignup"),
    path("ulogout/", ulogout , name="ulogout"),
    path("uchangepass/" , uchangepass , name="uchangepass"),
    path("about/", about , name="about"),

    path("todo/", todo , name="todo"),
    path("todocreate/" , todocreate , name="todocreate"),
    path("tododelete/<int:tid>/" , tododelete , name="tododelete"),
    path("todocomp/<int:tid>/" , todocomp, name="todocomp"),
    path("todoview/<int:tid>/", todoview , name="todoview"),

] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
