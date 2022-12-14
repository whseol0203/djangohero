# Generated by Django 4.1 on 2022-08-17 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_alter_comment_commentuser_alter_postinfo_postuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeUser', models.ForeignKey(db_column='likeUser', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userlike', to='board.auth')),
                ('targetPost', models.ForeignKey(db_column='targetPost', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='targetPost', to='board.postinfo')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
