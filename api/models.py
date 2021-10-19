from django.contrib.postgres.fields import JSONField
from django.db import models

"""
Abstract model which represent the important dates and state from the objects p. ex.
    YYYY-MM-DD HH:MM:SS,
    YYYY-MM-DD HH:MM:SS,
    active
"""
class StateCommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=False)
    status = models.CharField(max_length=35, null=False, default='active')

    class Meta:
        abstract = True


"""
Model which represent a property p. ex.
    Title,
    Address complete,
    Description,
    YYYY-MM-DD HH:MM:SS,
    YYYY-MM-DD HH:MM:SS,
    YYYY-MM-DD HH:MM:SS,
    active
"""
class Property(StateCommonInfo):
    title = models.CharField(max_length=255, null=False)
    address = models.TextField(null=False)
    description = models.TextField(null=False)
    disabled_at = models.DateTimeField(null=True)


"""
Model which represent a activity p. ex.
    id_property,
    YYYY-MM-DD HH:MM:SS,
    Title,
    YYYY-MM-DD HH:MM:SS,
    YYYY-MM-DD HH:MM:SS,
    active
"""
class Activity(StateCommonInfo):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    schedule = models.DateTimeField(null=False)
    title = models.CharField(max_length=255, null=False)

    def __str__(self):
            return self.title


"""
Model which represent a survey p. ex.
    id_activity,
    {'question':'answer'},
    YYYY-MM-DD
"""
class Survey(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)
    answers = JSONField(default=dict, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)