# Generated by Django 3.0.8 on 2020-07-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
