# Generated by Django 2.2.1 on 2019-05-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app25', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
