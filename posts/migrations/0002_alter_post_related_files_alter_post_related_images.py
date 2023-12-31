# Generated by Django 4.2.1 on 2023-10-04 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='related_files',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_relatedFiles', to='posts.relatedfile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='related_images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_relatedImages', to='posts.relatedimage'),
        ),
    ]
