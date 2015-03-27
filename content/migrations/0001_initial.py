# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('tags', models.TextField()),
                ('date', models.DateTimeField()),
                ('abstract', models.TextField()),
                ('image', models.FileField(upload_to=b'')),
                ('links', models.TextField()),
                ('category', models.ManyToManyField(to='content.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=50)),
                ('contents', models.ManyToManyField(to='content.Content')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
