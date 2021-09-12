from django.contrib.auth.models import User
from django.db import models


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    color = models.CharField(max_length=10, default='ffffff', null=False)  # hexadecimal color value
    starred = models.BooleanField(default=False, null=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Collaborator(models.Model):
    user = models.ForeignKey(User, related_name='collaborators', on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, related_name='collaborators', on_delete=models.CASCADE)
    # TODO: try to include the name
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.user)


class Task(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255, null=False)
    detail = models.TextField(null=True)
    isChecklist = models.BooleanField(default=False, null=False)
    done = models.BooleanField(default=False, null=False)
    priority = models.IntegerField(default=1, null=False, )  # higher number -> higher priority

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False)
    tasks = models.ManyToManyField(Task, related_name='tags')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
