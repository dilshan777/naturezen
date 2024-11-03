from djongo import models
from django.utils import timezone


class BPMRecord(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    first_bpm = models.FloatField(null=True, blank=True)  # First BPM recorded in the session
    last_bpm = models.FloatField(null=True, blank=True)   # Most recent BPM
    created_at = models.DateTimeField(default=timezone.now, editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, editable=True, null=True, blank=True)

    def __str__(self):
        return f"First BPM: {self.first_bpm}, Last BPM: {self.last_bpm}"

    class Meta:
        db_table = 'bpm_records'
