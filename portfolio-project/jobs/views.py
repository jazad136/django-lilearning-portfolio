   # Copyright 2022 Jonathan A. Saddler
   #
   # Licensed under the Apache License, Version 2.0 (the "License");
   # you may not use this file except in compliance with the License.
   # You may obtain a copy of the License at
   # http://www.apache.org/licenses/LICENSE-2.0
from django.shortcuts import render, get_object_or_404
from .models import Job
# Create your views here.
def homepage(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):
   # print(job_id)
   job_detail = get_object_or_404(Job, pk=job_id)
   return render(request, 'jobs/detail.html', {'job': job_detail})