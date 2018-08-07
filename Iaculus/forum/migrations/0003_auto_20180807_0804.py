# Generated by Django 2.1 on 2018-08-07 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_remove_post_report_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='closed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
