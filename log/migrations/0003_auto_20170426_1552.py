# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20170426_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcqquestion',
            name='answer',
            field=models.IntegerField(default=0, choices=[(0, b'A'), (1, b'B'), (2, b'C'), (3, b'D')]),
        ),
        migrations.AlterField(
            model_name='subquestion',
            name='category',
            field=models.CharField(max_length=50, choices=[(b'C', b'C'), (b'OS', b'Operating System'), (b'Micro', b'Microprossesor')]),
        ),
    ]
