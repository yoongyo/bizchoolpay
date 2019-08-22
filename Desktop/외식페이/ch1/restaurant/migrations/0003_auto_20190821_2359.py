# Generated by Django 2.1 on 2019-08-21 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20190821_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='category',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='menucategory',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='menucategory',
            name='restaurant',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='method',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='MenuCategory',
        ),
        migrations.DeleteModel(
            name='Method',
        ),
    ]
