# Generated by Django 3.1.1 on 2021-05-11 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='Policylist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='policyapp.policylist'),
        ),
    ]
