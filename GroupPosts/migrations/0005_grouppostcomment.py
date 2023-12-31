# Generated by Django 4.2.6 on 2023-10-13 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_rename_user_creategroup_admin_creategroup_members_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GroupPosts', '0004_grouppostlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('comment_file', models.FileField(blank=True, null=True, upload_to='')),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postComment_user', to=settings.AUTH_USER_MODEL)),
                ('commented_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postComment_post', to='GroupPosts.grouppost')),
                ('post_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postComment_group', to='groups.creategroup')),
            ],
        ),
    ]
