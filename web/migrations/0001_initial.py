# Generated by Django 3.2.12 on 2023-03-14 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=54)),
                ('Phone', models.CharField(max_length=10)),
                ('Massage', models.CharField(max_length=250)),
            ],
        ),
    ]