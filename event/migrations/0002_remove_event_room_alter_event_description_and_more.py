# Generated by Django 4.1.3 on 2022-11-29 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_delete_event'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='room',
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='from_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='to_date',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=200)),
                ('table_settings', models.CharField(max_length=200)),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('number_of_people', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
        ),
    ]
