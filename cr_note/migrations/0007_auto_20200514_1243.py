# Generated by Django 2.1.7 on 2020-05-14 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr_note', '0006_auto_20190515_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crn',
            name='cr_cash',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]