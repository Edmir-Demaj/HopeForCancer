# Generated by Django 3.2.18 on 2023-05-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230511_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
    ]
