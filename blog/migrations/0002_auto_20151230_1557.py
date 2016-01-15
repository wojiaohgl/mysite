# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.TextField()),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='blogPost',
            field=models.ForeignKey(to='blog.BlogPost'),
        ),
    ]
