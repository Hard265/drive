# Generated by Django 5.1.6 on 2025-03-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drive", "0003_remove_file_size_alter_file_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="size",
            field=models.BigIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]
