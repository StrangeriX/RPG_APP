# Generated by Django 4.0.5 on 2022-06-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_character_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(to='core.skill'),
        ),
    ]