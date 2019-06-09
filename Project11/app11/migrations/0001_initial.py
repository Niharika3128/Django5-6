# Generated by Django 2.1.5 on 2019-04-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('exp', models.DecimalField(decimal_places=2, max_digits=4)),
                ('designation', models.CharField(max_length=25)),
            ],
        ),
    ]
