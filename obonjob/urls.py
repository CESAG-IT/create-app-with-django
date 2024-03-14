
from django.contrib import admin
from django.urls import path
from jobs.views import home
from jobs.views import job_list, create_job, show_job 
from jobs.views import update_job, delete_job

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('jobs', job_list),
    path('new-job', create_job),
    path('show-job/<int:pk>', show_job),
    path('update-job/<int:pk>', update_job),
    path('delete-job/<int:pk>', delete_job)
]
