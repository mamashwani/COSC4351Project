# Generated by Django 2.2.7 on 2019-11-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_customuser_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='group_name',
            field=models.TextField(default='null', max_length=100),
        ),
    ]
