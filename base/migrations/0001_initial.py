# Generated by Django 4.1.2 on 2022-11-18 00:04

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
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('surname', models.CharField(max_length=250, null=True)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=250)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('birthday', models.DateField(null=True)),
                ('profile_photo', models.ImageField(upload_to='photos/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
