# Generated by Django 2.1.1 on 2018-09-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180929_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='texto_bonito',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_picture'),
        ),
    ]
