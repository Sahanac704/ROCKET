# Generated by Django 5.1 on 2024-09-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20)),
            ],
            options={
                'db_table': 'CSIT',
            },
        ),
    ]
