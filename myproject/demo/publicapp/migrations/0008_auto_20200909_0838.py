# Generated by Django 3.1 on 2020-09-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0007_tbl_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_cont',
            name='reply',
            field=models.CharField(default='Reply', max_length=100),
        ),
        migrations.AddField(
            model_name='tbl_cont',
            name='replymessage',
            field=models.CharField(default='........', max_length=100),
        ),
    ]