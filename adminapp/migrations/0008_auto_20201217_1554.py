# Generated by Django 2.2.17 on 2020-12-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_auto_20201217_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paket',
            name='hari_1',
            field=models.CharField(blank=True, choices=[('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu'), ('Minggu', 'Minggu')], max_length=200),
        ),
        migrations.AlterField(
            model_name='paket',
            name='hari_2',
            field=models.CharField(blank=True, choices=[('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu'), ('Minggu', 'Minggu')], max_length=200),
        ),
        migrations.AlterField(
            model_name='paket',
            name='hari_3',
            field=models.CharField(blank=True, choices=[('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu'), ('Minggu', 'Minggu')], max_length=200),
        ),
        migrations.AlterField(
            model_name='paket',
            name='hari_4',
            field=models.CharField(blank=True, choices=[('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu'), ('Minggu', 'Minggu')], max_length=200),
        ),
        migrations.AlterField(
            model_name='paket',
            name='jam_1',
            field=models.CharField(blank=True, choices=[('07-08 AM', '07-08 AM'), ('08-09 AM', '08-09 AM'), ('09-10 AM', '09-10 AM'), ('10-11 AM', '10-11 AM'), ('11-12 PM', '11-12 PM')], max_length=200),
        ),
        migrations.AlterField(
            model_name='paket',
            name='jam_2',
            field=models.CharField(blank=True, choices=[('07-08 AM', '07-08 AM'), ('08-09 AM', '08-09 AM'), ('09-10 AM', '09-10 AM'), ('10-11 AM', '10-11 AM'), ('11-12 PM', '11-12 PM')], max_length=200),
        ),
        migrations.AlterField(
            model_name='paket',
            name='jam_3',
            field=models.CharField(blank=True, choices=[('07-08 AM', '07-08 AM'), ('08-09 AM', '08-09 AM'), ('09-10 AM', '09-10 AM'), ('10-11 AM', '10-11 AM'), ('11-12 PM', '11-12 PM')], max_length=200),
        ),
        migrations.AlterField(
            model_name='paket',
            name='jam_4',
            field=models.CharField(blank=True, choices=[('07-08 AM', '07-08 AM'), ('08-09 AM', '08-09 AM'), ('09-10 AM', '09-10 AM'), ('10-11 AM', '10-11 AM'), ('11-12 PM', '11-12 PM')], max_length=200),
        ),
        migrations.AlterField(
            model_name='paket',
            name='jml_pertemuan',
            field=models.CharField(blank=True, choices=[('1X Pertemuan', '1X Pertemuan'), ('2X Pertemuan', '2X Pertemuan'), ('3X Pertemuan', '3X Pertemuan'), ('4X Pertemuan', '4X Pertemuan')], max_length=200, null=True),
        ),
    ]
