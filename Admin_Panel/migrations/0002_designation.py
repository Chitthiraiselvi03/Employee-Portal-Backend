# Generated by Django 4.1.3 on 2023-02-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
