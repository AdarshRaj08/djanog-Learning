# Generated by Django 5.0.6 on 2024-07-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]
