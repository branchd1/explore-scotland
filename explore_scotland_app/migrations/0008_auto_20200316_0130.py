# Generated by Django 3.0.3 on 2020-03-16 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore_scotland_app', '0007_auto_20200316_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='photos_liked', to='explore_scotland_app.UserProfile'),
        ),
    ]
