from django.db import models

class ResumeTemplate(models.Model):
    name = models.CharField(max_length=100)
    preview_image = models.ImageField(upload_to='templates/')

class UserResume(models.Model):
    template = models.ForeignKey(ResumeTemplate, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    summary = models.TextField()
