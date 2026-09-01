from django.contrib import admin
from .models import SiteSetting, Experience, Education, Project, Certification, Skill, ExtraCurricular, Reference

admin.site.register(SiteSetting)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Skill)
admin.site.register(ExtraCurricular)
admin.site.register(Reference)