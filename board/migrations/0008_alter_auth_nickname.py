# Generated by Django 4.1 on 2022-08-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_alter_auth_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='nickname',
            field=models.CharField(max_length=50),
        ),
    ]