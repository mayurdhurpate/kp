# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20150327_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='article_id',
            field=models.CharField(default=15, max_length=200),
            preserve_default=False,
        ),
    ]
