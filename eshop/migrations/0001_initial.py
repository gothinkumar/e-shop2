# Generated by Django 4.2.2 on 2023-07-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ComputerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('processor', models.CharField(max_length=90)),
                ('ram', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
