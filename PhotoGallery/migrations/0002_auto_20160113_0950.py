# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import PhotoGallery.ThumbnailImageField


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoGallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=PhotoGallery.ThumbnailImageField.ThumbnailImageField(upload_to=b'./photos'),
        ),
    ]
