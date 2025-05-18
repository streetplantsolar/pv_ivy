from rest_framework import serializers
from .models import User, IVCurveData, DiagnosticReport

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class IVDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IVCurveData
        fields = ('data_file',)

class DiagnosticReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticReport
        fields = ('id', 'generated_at', 'report_file')
