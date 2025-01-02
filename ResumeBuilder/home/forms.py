from django import forms
from .models import UserResume

class UserResumeForm(forms.ModelForm):
    class Meta:
        model = UserResume
        exclude = ('template',)


