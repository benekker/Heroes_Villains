# Generated by Django 4.0.6 on 2022-07-15 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('super_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Super',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alter_ego', models.CharField(max_length=100)),
                ('primary_ability', models.CharField(max_length=150)),
                ('secondary_ability', models.CharField(max_length=150)),
                ('catchphrase', models.CharField(max_length=200)),
                ('super_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='super_types.supertype')),
            ],
        ),
    ]
