# Generated by Django 2.1.5 on 2020-12-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='no_img.png', null=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
