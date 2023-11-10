# Generated by Django 4.2.7 on 2023-11-10 00:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classmate',
            name='address',
            field=models.CharField(default='Unknown', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classmate',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Unknown', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classmate',
            name='firstname',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Invalid Input:Only letters are allowed to the name.', regex='^[a-zA-Z]+$')]),
        ),
        migrations.AlterField(
            model_name='classmate',
            name='lastname',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Invalid Input:Only letters are allowed to the name.', regex='^[a-zA-Z]+$')]),
        ),
    ]