# Generated by Django 5.1.1 on 2024-11-29 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_alter_comment_visibility_alter_representation_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
    ]
