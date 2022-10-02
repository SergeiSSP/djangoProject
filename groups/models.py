import datetime

from django.core.validators import MinLengthValidator
from django.db import models
from .validators import validate_start_date

class Group(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Group Name',
        db_column='name',
        validators=[MinLengthValidator(2, "Group name must be greater than 1 character")]
    )
    start_date = models.DateField(
        default=datetime.date.today,
        null=True,
        blank=True,
        validators=[validate_start_date]
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'groups'