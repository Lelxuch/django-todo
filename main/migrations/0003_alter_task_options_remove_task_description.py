# Generated by Django 4.0.1 on 2022-01-19 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_options_remove_task_complete_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
