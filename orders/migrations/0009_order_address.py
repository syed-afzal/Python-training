# Generated by Django 3.1.4 on 2020-12-31 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20201231_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
