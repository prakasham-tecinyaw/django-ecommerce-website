# Generated by Django 3.1.2 on 2021-06-21 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_title', models.CharField(max_length=50, null=True)),
                ('image1', models.ImageField(upload_to='images')),
                ('image2', models.ImageField(upload_to='images')),
                ('image3', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_title', models.CharField(max_length=50, null=True)),
                ('cat_desc', models.TextField(null=True)),
                ('cat_status', models.IntegerField(choices=[(1, 'Active'), (0, 'Not Active')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100, null=True)),
                ('restaurant_address', models.CharField(max_length=200, null=True)),
                ('restaurant_delivery_duration', models.IntegerField(choices=[(10, '10 Minutes'), (20, '20 Minutes'), (30, '30 Minutes'), (40, '40 Minutes'), (50, '50 Minutes'), (60, '1 Hour')], default=20)),
                ('restaurant_status', models.IntegerField(choices=[(1, 'Active'), (0, 'Not Active')], default=1)),
                ('restaurant_opening_time', models.TimeField()),
                ('restaurant_closing_time', models.TimeField()),
                ('restaurant_logo', models.ImageField(default='images/default_logo.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100, null=True)),
                ('product_desc', models.TextField(null=True)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_status', models.IntegerField(choices=[(1, 'Active'), (0, 'Not Active')], default=1)),
                ('product_cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='shop.productcategory')),
                ('product_media', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='shop.mediagallery')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='shop.restaurant')),
            ],
        ),
    ]
