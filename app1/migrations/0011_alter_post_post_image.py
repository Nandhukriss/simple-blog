# Generated by Django 4.2.6 on 2023-12-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='uploads/Posts/default.png', upload_to='Posts'),
        ),
    ]