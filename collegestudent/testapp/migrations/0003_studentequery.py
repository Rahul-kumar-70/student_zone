# Generated by Django 5.1.5 on 2025-04-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_studentphd'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentEquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('Mobile', models.BigIntegerField()),
                ('Email_id', models.CharField(max_length=64)),
                ('Course', models.CharField(max_length=64)),
                ('Address', models.CharField(max_length=64)),
            ],
        ),
    ]
