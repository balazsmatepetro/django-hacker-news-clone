# Generated by Django 3.2.7 on 2021-09-08 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsitem',
            options={'ordering': ['-created_at']},
        ),
    ]
