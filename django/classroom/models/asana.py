from django.db import models


class Workspace(models.Model):
    name = models.CharField(max_length=20)


class Project(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.deletion.CASCADE)


class Section(models.Model):
    project = models.ForeignKey(Project, on_delete=models.deletion.CASCADE)
    name = models.CharField(max_length=20)


class Task(models.Model):
    section = models.ForeignKey(Workspace, on_delete=models.deletion.CASCADE)
    name = models.CharField(max_length=20)


class CustomTextFieldDefinition(models.Model):
    field_name = models.CharField(max_length=20)


class TaskCustomTextFieldValue(models.Model):
    task = models.ForeignKey(Task)
    text_field_definition = models.ForeignKey(CustomTextFieldDefinition)
    field_value = models.CharField(max_length=20)


class WorkspaceCustomTextFieldValue(models.Model):
    workspace = models.ForeignKey(Workspace)
    text_field_definition = models.ForeignKey(CustomTextFieldDefinition)
    field_value = models.CharField(max_length=20)
