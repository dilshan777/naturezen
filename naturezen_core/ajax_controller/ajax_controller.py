import json
from django.http import JsonResponse
from django.utils import timezone
from naturezen_core.models import BPMRecord


# Helper function to update BPMRecord in the database
def update_bpm_record(bpm_value, request):
    current_date = timezone.now().date()

    # Get the record for the current user
    record = BPMRecord.objects.filter(username=request.user.username).last()

    if record:
        # Check if the date of the record is different from today
        if record.created_at.date() != current_date:
            # Create a new record for a new date
            record = BPMRecord(
                username=request.user.username,
                first_bpm=bpm_value,
                last_bpm=bpm_value,
                created_at=timezone.now(),  # Set current date
                updated_at=timezone.now()
            )
            record.save()
        else:
            # Update the existing record
            record.last_bpm = bpm_value
            record.updated_at = timezone.now()  # Update the timestamp
            record.save()
    else:
        # If no record exists, create a new one
        record = BPMRecord(
            username=request.user.username,
            first_bpm=bpm_value,
            last_bpm=bpm_value,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        record.save()


def update_bpm(request):
    if request.method == "POST":
        try:
            bpm_value = json.loads(request.body)
            if bpm_value is not None:
                update_bpm_record(float(bpm_value), request)
                return JsonResponse({"status": "success"})
        except (json.JSONDecodeError, ValueError) as e:
            return JsonResponse({"status": "failed", "error": str(e)}, status=400)
    return JsonResponse({"status": "failed"}, status=400)
