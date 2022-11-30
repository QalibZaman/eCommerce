# Generated by Django 4.1.2 on 2022-11-29 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_sharing_following'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('description', models.TextField(max_length=250, null=True)),
                ('price', models.FloatField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]