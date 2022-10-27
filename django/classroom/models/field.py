from enum import Enum
from django.db import models


class EntityType(Enum):
    SCHOOL = "school"
    GRADE = "grade"
    CLASSROOM = "classroom"

class FieldDefinition(models.Model):
    name = models.CharField(max_length=30)
    entity_type = models.TextChoices(choices=EntityType.__)


class CustomField(models.Model):
    pass
