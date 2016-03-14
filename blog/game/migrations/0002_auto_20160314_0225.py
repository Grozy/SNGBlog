# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gameinfo',
            options={'verbose_name': '\u6e38\u620f\u4fe1\u606f'},
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='body',
            field=models.TextField(verbose_name=b'\xe8\xaf\xa6\xe6\x83\x85'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='timestamp',
            field=models.DateTimeField(verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='title',
            field=models.CharField(max_length=150, verbose_name=b'\xe6\xb8\xb8\xe6\x88\x8f\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=True,
        ),
    ]
