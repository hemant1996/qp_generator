# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcqquestion',
            name='difficulty',
            field=models.IntegerField(choices=[(2, b'hard'), (1, b'medium'), (0, b'easy')]),
        ),
        migrations.AlterField(
            model_name='subquestion',
            name='difficulty',
            field=models.IntegerField(choices=[(2, b'hard'), (1, b'medium'), (0, b'easy')]),
        ),
    ]
