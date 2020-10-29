# Generated by Django 3.1.1 on 2020-09-30 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Test_Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_Sequence', models.CharField(max_length=200)),
                ('condition', models.CharField(max_length=200)),
                ('test_date', models.DateTimeField(verbose_name='date tested')),
                ('isc', models.FloatField(default=0)),
                ('voc', models.FloatField(default=0)),
                ('imp', models.FloatField(default=0)),
                ('vmp', models.FloatField(default=0)),
                ('ff', models.FloatField(default=0)),
                ('pmp', models.FloatField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]