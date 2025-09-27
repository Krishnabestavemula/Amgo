from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.contrib.auth.models import UserManager

class UserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Asset(models.Model):
    project = models.ForeignKey(Project, related_name='assets', on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_assets/')



class Job(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('done', 'Done'),
        ('failed', 'Failed'),
    ]
    project = models.ForeignKey(Project, related_name='jobs', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.project.title} - {self.status}"


class AnalyticsEvent(models.Model):
    EVENT_TYPES = [
        ("play", "Play"),
        ("click", "Click"),
        ("impression", "Impression"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="analytics_events")
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title} - {self.event_type} at {self.timestamp}"
