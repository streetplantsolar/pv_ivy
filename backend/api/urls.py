from django.urls import path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="home/landing_page.html"), name='landing-page'),
    path('auth/register/', TemplateView.as_view(template_name="home/landing_page.html"), name='signup'),  # Reuse the same template,
    path('auth/login/', obtain_auth_token, name='login'),
    path('iv-data/upload/', views.IVDataUploadView.as_view(), name='iv_data_upload'),
    path('diagnostics/', views.DiagnosticsView.as_view(), name='diagnostics')
]
