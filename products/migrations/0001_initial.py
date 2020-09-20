# Generated by Django 3.1.1 on 2020-09-20 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField()),
                ('quantity', models.DecimalField(decimal_places=1, max_digits=100)),
                ('unit', models.CharField(max_length=20)),
                ('isForSale', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisations.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=1, max_digits=100)),
                ('unit', models.CharField(max_length=20)),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
        ),
    ]
