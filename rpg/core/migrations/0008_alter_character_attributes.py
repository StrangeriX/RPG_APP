# Generated by Django 4.0.5 on 2022-06-11 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_character_attributes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='attributes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.attribute'),
        ),
    ]
