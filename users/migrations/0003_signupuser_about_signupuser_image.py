# Generated by Django 4.2.1 on 2023-10-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_signupuser_grade_alter_signupuser_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupuser',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='signupuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
