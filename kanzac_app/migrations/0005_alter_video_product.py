# Generated by Django 4.1.7 on 2023-03-22 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanzac_app', '0004_product_descr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='kanzac_app.product'),
        ),
    ]
