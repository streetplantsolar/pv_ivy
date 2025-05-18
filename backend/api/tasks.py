from celery import shared_task
from .models import IVCurveData, DiagnosticReport
import time

@shared_task
def process_iv_data_task(iv_data_id):
    try:
        iv_data = IVCurveData.objects.get(id=iv_data_id)
        time.sleep(5)
        DiagnosticReport.objects.create(
            user=iv_data.user,
            iv_curve_data=iv_data,
            report_file='path/to/dummy_report.pdf'
        )
        iv_data.processed = True
        iv_data.save()
    except IVCurveData.DoesNotExist:
        pass
