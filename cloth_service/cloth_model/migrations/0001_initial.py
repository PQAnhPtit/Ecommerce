# Generated by Django 4.1.7 on 2023-03-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cloth_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_id', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('cloth_name', models.CharField(max_length=100)),
                ('availability', models.CharField(max_length=15)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]