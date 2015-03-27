# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20150327_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='abstract',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.FileField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='links',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='tags',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='contents',
            field=models.ManyToManyField(to='content.Content', null=True, blank=True),
            preserve_default=True,
        ),
    ]
