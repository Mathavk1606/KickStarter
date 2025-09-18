from django.shortcuts import render
from .models import Chat, StartupAnalysis
import json

def index(request):
    chats = Chat.objects.all().order_by('-timestamp')[:10]
    analyses = StartupAnalysis.objects.all().order_by('-created_at')[:1]

    if request.method == 'POST':
        message = request.POST.get('message')
        file = request.FILES.get('file')
        if message or file:
            Chat.objects.create(user="User", message=message or "", file=file)

        # Simulate AI analysis (replace with Google AI integration)
        if message:
            analysis_data = {
                'company_name': 'Sample Startup',
                'sector': 'Tech',
                'financial_multiples': {'revenue': 1000000, 'growth_rate': 0.2},
                'hiring_data': {'headcount': 50, 'new_hires': 10},
                'traction_signals': {'customers': 1000, 'retention': 0.85},
                'risk_indicators': {'churn': 'Low', 'metrics_consistency': 'High'},
                'growth_potential': 'Strong growth potential in SaaS market.',
                'recommendations': 'Invest with focus on scaling operations.'
            }
            StartupAnalysis.objects.create(**analysis_data)

    return render(request, 'index.html', {'chats': chats, 'analyses': analyses})
