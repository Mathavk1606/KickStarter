from django.db import models

class Chat(models.Model):
    user = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.timestamp}"

class StartupAnalysis(models.Model):
    company_name = models.CharField(max_length=200)
    sector = models.CharField(max_length=100)
    financial_multiples = models.JSONField()
    hiring_data = models.JSONField()
    traction_signals = models.JSONField()
    risk_indicators = models.JSONField()
    growth_potential = models.TextField()
    recommendations = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
