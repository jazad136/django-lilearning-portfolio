   # Copyright 2022 Jonathan A. Saddler
   #
   # Licensed under the Apache License, Version 2.0 (the "License");
   # you may not use this file except in compliance with the License.
   # You may obtain a copy of the License at
   # http://www.apache.org/licenses/LICENSE-2.0 
from django.contrib import admin
from .models import Job

# Register your models here.
admin.site.register(Job)