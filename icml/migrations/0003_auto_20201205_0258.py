# Generated by Django 3.1.3 on 2020-12-04 21:28

from django.db import migrations, models
import icml.storage


class Migration(migrations.Migration):

    dependencies = [
        ('icml', '0002_auto_20201205_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(storage=icml.storage.OverwriteStorage(), upload_to='media\\images'),
        ),
    ]
