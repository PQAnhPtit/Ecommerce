# Generated by Django 4.1.7 on 2023-03-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='img_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=10)),
            ],
        ),
    ]
