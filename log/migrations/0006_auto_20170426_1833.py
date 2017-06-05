# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_textfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='McqTextFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mcq', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/path/to/mcq'), upload_to=b'')),
                ('answer', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/path/to/answer'), upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='SubTextFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/path/to/mcq'), upload_to=b'')),
            ],
        ),
        migrations.DeleteModel(
            name='TextFile',
        ),
    ]
