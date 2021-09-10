from django.contrib.auth.models import User
from django.db import models


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    color = models.CharField(max_length=10, default='ffffff', null=False)  # hexadecimal color value
    starred = models.BooleanField(default=False, null=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Collaborator(models.Model):
    user = models.ManyToManyField(User)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.user.name

    class Meta:
        pass


class Task(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, )
    name = models.CharField(max_length=255, null=False)
    detail = models.TextField(null=True)
    is_checklist = models.BooleanField(default=False, null=False)
    done = models.BooleanField(default=False, null=False)
    priority = models.IntegerField(default=1, null=False, )  # higher number -> higher priority

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False)
    task = models.ManyToManyField(Task)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
