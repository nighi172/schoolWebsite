# Generated by Django 3.0.8 on 2020-07-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0002_tbl_cont'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
