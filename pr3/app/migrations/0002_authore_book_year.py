# Generated by Django 5.1.1 on 2024-09-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(default=2000, max_length=10),
            preserve_default=False,
        ),
    ]
