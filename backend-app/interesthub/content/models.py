from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# from components.models import Component

# Create your models here.

class ContentType(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40, blank=True, null=True)

    TEXT = "text"
    LONGTEXT = "longtext"
    NUMBER = "number"
    DATETIME = "datetime"
    IMAGE = "image"
    VIDEO = "video"
    DROPDOWN = "dropdown"
    CHECKBOX = "checkbox"
    TYPE_CHOICES = (
        (TEXT, "Text"),
        (LONGTEXT, "Long Text"),
        (NUMBER, "Number"),
        (DATETIME, "Date/Time"),
        (IMAGE, "Image"),
        (VIDEO, "Video"),
        (DROPDOWN, "Dropdown"),
        (CHECKBOX, "Checkbox"),
    )

    # this can be converted to choices
    components = ArrayField(
        models.CharField(max_length=10, choices=TYPE_CHOICES, blank=True),
        size=15,
    )

    component_names = ArrayField(
        models.CharField(max_length=50, blank=False),
        size=15,
        null=True
    )

    def __str__(self):
        return self.name

class Content(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, blank=True, null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="content_owner")
    
    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    text = models.TextField(null=False, blank=True)
    owner = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="comment_owner")
    content = models.ForeignKey(Content, blank=False, null=False, on_delete=models.CASCADE, related_name="comments")
        
    def __str__(self):
        return str(self.id)

class UpDown(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="vote_owner")
    content = models.ForeignKey(Content, blank=False, null=False, on_delete=models.CASCADE, related_name="votes")
    isUp = models.BooleanField(default=True)
        
    def __str__(self):
        return str(self.id)
