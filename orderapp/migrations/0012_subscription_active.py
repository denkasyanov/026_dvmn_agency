# Generated by Django 3.2.18 on 2023-02-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0011_rename_description_messages_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Активен'),
        ),
    ]
