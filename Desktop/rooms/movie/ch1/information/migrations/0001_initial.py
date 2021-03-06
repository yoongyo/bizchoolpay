# Generated by Django 2.0 on 2019-03-10 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fullName', models.CharField(max_length=100)),
                ('CEO', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('Email', models.EmailField(max_length=254)),
                ('Tel', models.CharField(max_length=30)),
                ('bank', models.CharField(max_length=50)),
                ('event', models.TextField()),
                ('businessLicense', models.CharField(max_length=50)),
                ('businessHours', models.CharField(max_length=100)),
            ],
        ),
    ]
