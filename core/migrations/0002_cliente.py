# Generated by Django 5.1.4 on 2024-12-31 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estoque', models.EmailField(max_length=100, verbose_name='E-mail')),
            ],
        ),
    ]
