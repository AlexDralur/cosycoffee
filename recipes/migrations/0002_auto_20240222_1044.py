# Generated by Django 3.2.23 on 2024-02-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='grinding_size',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
