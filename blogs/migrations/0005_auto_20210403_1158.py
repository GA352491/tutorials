# Generated by Django 3.1.7 on 2021-04-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20210403_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.ImageField(upload_to='blogs/static/media'),
        ),
    ]
