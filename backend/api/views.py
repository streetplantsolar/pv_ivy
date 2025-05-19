from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .models import User, IVCurveData, DiagnosticReport
from .serializers import RegisterSerializer, IVDataSerializer, DiagnosticReportSerializer
from .tasks import process_iv_data_task

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IVDataUploadView(APIView):
    def post(self, request):
        serializer = IVDataSerializer(data=request.data)
        if serializer.is_valid():
            iv_data = serializer.save(user=request.user)
            process_iv_data_task.delay(iv_data.id)
            return Response({'message': 'Data uploaded successfully. Processing initiated.'}, status=status.HTTP_201_CREATED)
        else:
            send_mail(
                'Invalid Data Upload - PV Ivy',
                'Your recent data upload was invalid. Please check and try again.',
                'no-reply@pvivy.com',
                [request.user.email],
                fail_silently=True,
            )
            raise ValidationError({'error': 'Invalid data. Please check your upload.'})

class DiagnosticsView(APIView):
    def get(self, request):
        reports = DiagnosticReport.objects.filter(user=request.user)
        serializer = DiagnosticReportSerializer(reports, many=True)
        return Response({'reports': serializer.data}, status=status.HTTP_200_OK)
