# Generated by Django 4.0.4 on 2022-04-28 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_rename_text_topic_anything'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='anything',
            new_name='poshel_nafig',
        ),
    ]
