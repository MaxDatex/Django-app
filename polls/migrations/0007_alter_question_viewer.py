# Generated by Django 3.2.4 on 2021-06-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20210607_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='viewer',
            field=models.ManyToManyField(to='polls.Viewer'),
        ),
    ]
