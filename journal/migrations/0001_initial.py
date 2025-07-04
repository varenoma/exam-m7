# Generated by Django 5.2.2 on 2025-06-07 13:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('pdf', models.FileField(upload_to='journal/pdf/')),
                ('technologies', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='journal/avatar/')),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'journal',
            },
        ),
    ]
