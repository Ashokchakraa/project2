# Generated by Django 4.0.5 on 2022-10-19 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyProducts', '0002_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='CostItem',
            new_name='costPerItem',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='StockQuantity',
            new_name='stockQuantity',
        ),
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
