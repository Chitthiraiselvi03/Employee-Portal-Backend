# Generated by Django 4.1.3 on 2023-02-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Panel', '0002_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]