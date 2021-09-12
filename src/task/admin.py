from django.contrib import admin

from .models import Collection, Tag, Task, Collaborator

admin.site.register(Collection)
admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(Collaborator)
