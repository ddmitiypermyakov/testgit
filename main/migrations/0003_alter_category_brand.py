# Generated by Django 3.2.7 on 2021-10-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='brand',
            field=models.TextField(),
        ),
    ]
