# Generated by Django 2.2.1 on 2019-06-07 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Reporter')),
            ],
        ),
    ]
