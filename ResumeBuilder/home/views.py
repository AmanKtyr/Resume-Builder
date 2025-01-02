from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def  ResumeBuilder(request):
    return render(request, 'home/ResumeBuilder.html')

def choose_template(request):
    templates = ResumeTemplate.objects.all()
    return render(request, 'home/choose_template.html', {'templates': templates})


# for form handling
def fill_form(request, template_id):
    template = get_object_or_404(ResumeTemplate, id=template_id)
    if request.method == 'POST':
        form = UserResumeForm(request.POST)
        if form.is_valid():
            user_resume = form.save(commit=False)
            user_resume.template = template
            user_resume.save()
            return redirect('preview_resume', user_resume.id)
    else:
        form = UserResumeForm()
    return render(request, 'home/fill_form.html', {'form': form, 'template': template})



def download_resume(request, resume_id):
    resume = get_object_or_404(UserResume, id=resume_id)
    template = get_template('home/preview_resume.html')
    html = template.render({'resume': resume})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{resume.full_name}_Resume.pdf"'

    # Convert HTML to PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors while generating the PDF', status=500)
    return response
def preview_resume(request, resume_id):
    # Retrieve the resume based on the provided `resume_id`
    resume = get_object_or_404(UserResume, id=resume_id)
    
    # Render a template for the resume preview
    return render(request, 'home/preview_resume.html', {'resume': resume})