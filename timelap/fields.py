from django.db import models
from django.utils.six import with_metaclass


class DateRangeField(with_metaclass(models.SubfieldBase, models.Field)):
	# Attributes
	description = _("A basic date range field")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 21
        super(HandField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(HandField, self).deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def db_type(self, connection):
        return 'char(21)'

    def to_python(self, value):
    	# None case for null = True
        if value is None:
            return value
        # Not none python object case
    	else:
    		pass
        # The string case.
        pass
