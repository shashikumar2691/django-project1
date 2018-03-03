# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_employee_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Employee'),
        ),
    ]
