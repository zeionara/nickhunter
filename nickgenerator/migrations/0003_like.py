# Generated by Django 2.1 on 2018-08-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nickgenerator', '0002_nick_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=20)),
                ('nick_title', models.CharField(max_length=64)),
            ],
        ),
    ]