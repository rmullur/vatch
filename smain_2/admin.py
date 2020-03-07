from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import Video
from django.db import models

'''class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
'''

##admin.site.register(Item)
admin.site.register(Video)

# Register your models here.
