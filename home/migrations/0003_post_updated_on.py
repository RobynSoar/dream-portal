# Generated by Django 4.2.18 on 2025-01-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
