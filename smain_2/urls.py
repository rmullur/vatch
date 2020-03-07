from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'smain_2'

urlpatterns = [
        path("",views.homepage,name="homepage"),
        path("register",views.register,name="register"),
        path("logout",views.logout_request, name="logout"),
        path("login",views.login_request, name="login"),
        path("help",views.help_request, name="help"),
        path("account",views.account_request, name="account"),
        path("stream/<slug:username>/",views.stream, name="stream_ref"),
        path("viewstream/<slug:stream_key>/",views.watch_video, name="video_viewer"),

        ] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
