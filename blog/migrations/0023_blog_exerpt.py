# Generated by Django 3.1.5 on 2022-12-09 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20221201_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='exerpt',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
