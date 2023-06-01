# Generated by Django 4.2.1 on 2023-05-25 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(blank=True, max_length=15, null=True)),
                ('street_number', models.IntegerField(blank=True, max_length=15, null=True)),
                ('city', models.IntegerField(blank=True, max_length=13, null=True)),
                ('state', models.IntegerField(blank=True, max_length=12, null=True)),
                ('country', models.IntegerField(blank=True, max_length=14, null=True)),
                ('pincode', models.IntegerField(blank=True, max_length=3, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customers')),
            ],
        ),
    ]
