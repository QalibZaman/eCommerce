# Generated by Django 4.1.2 on 2022-11-30 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_userdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='profile_photo',
            field=models.ImageField(upload_to='base/static/photos/'),
        ),
    ]
