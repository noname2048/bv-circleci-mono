from django.db import models


class FieldDefinition(models.Model):
    name = models.CharField(max_length=30)
    entity_type = models.CharField(choices=EntityType.choices)

    class EntityType(models.TextChoices):
        SCHOOL = "school"
        GRADE = "grade"
        CLASSROOM = "classroom"


class CustomField(models.Model):
    pass
