# Generated by Django 3.2.5 on 2021-09-22 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezyaplyapp', '0005_auto_20210922_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('an_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=200, null=True)),
                ('announcement_text', models.TextField(max_length=1000, null=True)),
            ],
        ),
    ]
