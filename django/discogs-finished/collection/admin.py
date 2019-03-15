from django.contrib import admin

# Register your models here.
from .models import Artist, Release, Track

admin.site.register(Artist)
admin.site.register(Release)
admin.site.register(Track)