# Generated by Django 5.1.1 on 2024-10-08 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('category_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ProductCategory', to='products.productcategory'),
            preserve_default=False,
        ),
    ]
