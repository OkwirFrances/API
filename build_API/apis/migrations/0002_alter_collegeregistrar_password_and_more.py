# Generated by Django 4.2.17 on 2025-03-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeregistrar',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='collegeregistrar',
            name='role',
            field=models.CharField(default='registrar', max_length=10),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='role',
            field=models.CharField(default='lecturer', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='student',
            name='role',
            field=models.CharField(default='student', max_length=10),
        ),
    ]
