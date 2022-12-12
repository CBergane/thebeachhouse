# Generated by Django 3.2.16 on 2022-12-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('category', models.CharField(choices=[('BAS', 'BASIC'), ('LUX', 'LUXURIUS'), ('KIN', 'KING'), ('QUE', 'QUEEN')], max_length=3)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]