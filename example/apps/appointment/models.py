from django.db import models
from django.utils.translation import ugettext as _
from timelap.models import ModelWithDateRange, ModelWithDateTimeRange


class SimpleEvent(ModelWithDateRange):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)

	class Meta(ModelWithDateRange.Meta):
		verbose_name = _('Simple Event')
		verbose_name_plural = _('Simple Events')


class ClassicEvent(ModelWithDateTimeRange):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)

	class Meta(ModelWithDateTimeRange.Meta):
		verbose_name = _('Classic Event')
		verbose_name_plural = _('Classic Events')
