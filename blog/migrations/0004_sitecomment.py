# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160105_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.TextField()),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
