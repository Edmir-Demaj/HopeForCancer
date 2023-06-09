# Generated by Django 3.2.18 on 2023-05-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230506_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text="Share your inspiring cancer story with us. Your words can make a difference in someone's life.", max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='describe_image',
            field=models.CharField(default='A default image.', help_text='Please provide a short description for your image', max_length=70),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Please provide a descriptive title for your post. Maximum length is 60 characters.', max_length=60, unique=True),
        ),
    ]
