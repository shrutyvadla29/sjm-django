from django.urls import path
from . import views

urlpatterns=[
    path("", view=views.homepage, name="homepage"),
    path("about/", view=views.aboutpage, name="aboutpage"),
    path("login/", view=views.login_page,name="login_view"),
    path("signup/", view=views.signup_page, name="signup"),
    path("publications/", view=views.publications_page, name="publications"),
    path("publication/<slug:slug>/", views.publication_detail, name="publication_detail"),
    path("logout/", view=views.logout_view, name="logout"),
]