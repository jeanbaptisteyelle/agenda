# Generated by Django 2.2.12 on 2020-07-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='organisateurs',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='prix',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='lieu',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
