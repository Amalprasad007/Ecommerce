# Generated by Django 5.0.2 on 2024-03-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooduser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='commensettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=250, null=True)),
                ('amounts', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
