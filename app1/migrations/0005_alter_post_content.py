# Generated by Django 4.2.6 on 2023-11-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_post_category_post_blog_content_post_doc_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=250),
        ),
    ]
