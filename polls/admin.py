from django.contrib import admin

from .models import Question, Viewer


admin.site.register(Viewer)
admin.site.register(Question)
