# Generated by Django 2.1.7 on 2019-04-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr_note', '0002_auto_20190409_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='crn',
            name='amount_in_words',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='crn',
            name='cr_cash',
            field=models.IntegerField(null=True),
        ),
    ]
