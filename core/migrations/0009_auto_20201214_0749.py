# Generated by Django 3.1.2 on 2020-12-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20201213_0240'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AddField(
            model_name='producto',
            name='numeroIdentificador',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
