# Generated by Django 3.2.21 on 2023-11-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vgallery',
            fields=[
                ('vgallery_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=45)),
                ('classes', models.CharField(max_length=45)),
                ('date', models.CharField(blank=True, max_length=45, null=True)),
                ('images', models.CharField(max_length=545)),
                ('videos', models.CharField(max_length=545)),
            ],
            options={
                'db_table': 'vgallery',
                'managed': False,
            },
        ),
    ]
