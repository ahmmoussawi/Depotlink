# Generated by Django 5.0.1 on 2024-01-30 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_rename_company_firm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='defaultcategory.png', null=True, upload_to='categories/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='defaultitem.png', null=True, upload_to='items/'),
        ),
    ]