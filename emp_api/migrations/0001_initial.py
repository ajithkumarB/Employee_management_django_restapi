# Generated by Django 2.1.5 on 2019-09-11 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=255)),
                ('mobile_no', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
