# Generated by Django 2.2.5 on 2019-11-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191011_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pval',
            name='PVALUE',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=22, max_length=100, null=True),
        ),
    ]
