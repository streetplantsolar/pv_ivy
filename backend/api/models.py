from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class IVCurveData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    data_file = models.FileField(upload_to='iv_data/')
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"IV Data - {self.user.email} - {self.uploaded_at}"

class DiagnosticReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    iv_curve_data = models.ForeignKey(IVCurveData, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)
    report_file = models.FileField(upload_to='reports/')

    def __str__(self):
        return f"Report - {self.user.email} - {self.generated_at}"

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notification_preferences = models.JSONField(default=dict)

    def __str__(self):
        return f"Settings - {self.user.email}"
