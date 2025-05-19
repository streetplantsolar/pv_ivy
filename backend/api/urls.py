from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/login/', obtain_auth_token, name='login'),
    path('iv-data/upload/', views.IVDataUploadView.as_view(), name='iv_data_upload'),
    path('diagnostics/', views.DiagnosticsView.as_view(), name='diagnostics'),
    path('api/', include('backend.api.urls'))
]
