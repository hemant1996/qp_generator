# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20170426_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcqquestion',
            name='category',
            field=models.CharField(default=b'C', max_length=50, choices=[(b'C', b'C'), (b'OS', b'Operating System'), (b'Micro', b'Microprossesor')]),
        ),
    ]
