# Generated by Django 2.2.11 on 2020-04-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20200407_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cuis_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]