# Generated by Django 4.1 on 2022-08-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_likeinfo_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='postinfo',
            name='views',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
