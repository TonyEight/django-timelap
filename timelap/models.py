from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


__all__ = ['ModelWithDateRange', 'ModelWithDateTimeRange',]


class ModelWithDateRange(models.Model):
    # Attributes
    start_date = models.DateField()
    end_date = models.DateField()

    # Methods
    def clean(self):
        if self.start_date and self.end_date\
        and self.start_date > self.end_date:
            raise ValidationError(_('End date must be greater or ' \
                                    'equal to start date.'))

    # Meta-data
    class Meta:
        abstract = True


class ModelWithDateTimeRange(models.Model):
    # Attributes
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    # Methods
    def clean(self):
        if self.start_datetime and self.end_datetime\
        and self.start_datetime > self.end_datetime:
            raise ValidationError(_('End datetime must be greater or equal' \
                                    ' to start datetime.'))

    # Meta-data
    class Meta:
        abstract = True
