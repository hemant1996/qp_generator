# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0008_auto_20170426_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcqquestion',
            name='category',
            field=models.IntegerField(default=b'C', choices=[(0, b'C'), (1, b'Operating System'), (2, b'Microprossesor')]),
        ),
        migrations.AlterField(
            model_name='subquestion',
            name='category',
            field=models.IntegerField(choices=[(0, b'C'), (1, b'Operating System'), (2, b'Microprossesor')]),
        ),
    ]
