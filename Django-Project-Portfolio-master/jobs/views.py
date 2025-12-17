from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def Home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})

def show_details(request, job_id):
    job=get_object_or_404(Job, id=job_id)
    return render(request, "jobs/job_details.html", {"job_details":job})