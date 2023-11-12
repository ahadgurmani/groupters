# Generated by Django 4.2.1 on 2023-10-03 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Decline', 'Decline'), ('Accept', 'Accept')], default='Pending', max_length=20, null=True)),
                ('connection_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connectionBy_user', to=settings.AUTH_USER_MODEL)),
                ('connection_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connectionTo_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
