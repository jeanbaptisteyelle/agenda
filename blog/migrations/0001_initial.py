# Generated by Django 2.2.12 on 2020-09-11 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('date_add', models.DateField(auto_now=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('prix', models.FloatField()),
                ('description', models.TextField()),
                ('organisateurs', models.TextField()),
                ('speackers', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(upload_to='image/Event')),
                ('date_add', models.DateField(auto_now=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie_Event', to='blog.Categorie')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('marp_url', models.TextField()),
                ('telephone', models.IntegerField()),
                ('adresse', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('date_add', models.DateField(auto_now=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Lieu',
                'verbose_name_plural': 'Lieux',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image/Partner')),
                ('lien', models.URLField()),
                ('date_add', models.DateField(auto_now=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('date_add', models.DateField(auto_now=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='image/new')),
                ('date_add', models.DateField(auto_now=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_new', to='blog.Event')),
            ],
            options={
                'verbose_name': 'New',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='lieu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lieu_Event', to='blog.Lieu'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
