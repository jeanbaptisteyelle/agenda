# Generated by Django 2.2.12 on 2020-07-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200703_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='speackers',
            field=models.CharField(max_length=255, null=True),
        ),
    ]