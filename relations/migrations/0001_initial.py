# Generated by Django 4.2.6 on 2023-10-11 10:15

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProdctImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodcut_image', to='relations.product')),
            ],
        ),
    ]
