# Generated by Django 3.0.1 on 2021-02-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0013_auto_20210209_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='payment_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='payment_method',
            field=models.CharField(choices=[('Khalti', 'Khalti')], default='Khalti', max_length=20),
        ),
    ]
