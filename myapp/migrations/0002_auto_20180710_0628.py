# Generated by Django 2.0.7 on 2018-07-10 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.CharField(max_length=200),
        ),
    ]