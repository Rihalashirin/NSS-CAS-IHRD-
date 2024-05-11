# Generated by Django 3.2.21 on 2023-11-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('report', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'report',
                'managed': False,
            },
        ),
    ]
