# Generated by Django 3.1.1 on 2020-11-09 14:39

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
    ]
