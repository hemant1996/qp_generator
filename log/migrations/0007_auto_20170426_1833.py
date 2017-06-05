# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0006_auto_20170426_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtextfile',
            name='sub',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/path/to/sub'), upload_to=b''),
        ),
    ]
