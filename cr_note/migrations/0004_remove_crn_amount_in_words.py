# Generated by Django 2.1.7 on 2019-04-09 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cr_note', '0003_auto_20190409_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crn',
            name='amount_in_words',
        ),
    ]
