from django.db import models

class Professional(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)
    domain = models.CharField(max_length=200)
    expertise_area = models.TextField(blank=True)
    expertise_tools = models.TextField(blank=True)   # comma-separated list OK
    manual_tools = models.TextField(blank=True)
    navratnas = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.designation}"
