# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tvapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 8, 12, 24, 31, 945659, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
