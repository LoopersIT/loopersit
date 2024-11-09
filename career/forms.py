from django import forms
from .models import Application, Job


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['role','name', 'email', 'mobile_number', 'salary_expectation', 'cv']

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        active_jobs = Job.objects.filter(active=True)
        self.fields['role'].choices = [(job.title, job.title) for job in active_jobs]