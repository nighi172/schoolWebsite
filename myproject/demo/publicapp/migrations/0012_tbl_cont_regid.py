# Generated by Django 3.1 on 2020-10-01 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0011_remove_tbl_log_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_cont',
            name='regid',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
