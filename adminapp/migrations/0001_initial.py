# Generated by Django 2.2.17 on 2020-12-16 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataguru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('nohp', models.CharField(max_length=15)),
                ('alamat', models.CharField(max_length=225, null=True)),
                ('biaya', models.IntegerField(blank=True)),
                ('no_id', models.IntegerField()),
                ('kelamin', models.BooleanField(default=True)),
                ('usia', models.IntegerField(blank=True, null=True)),
                ('link', models.CharField(max_length=100, null=True)),
                ('catatan', models.TextField(null=True)),
                ('foto', models.ImageField(upload_to='img/')),
                ('portofolio', models.FileField(upload_to='document/')),
            ],
        ),
        migrations.CreateModel(
            name='hari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NamaHari', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='KtgAmpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='paket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NamaPaket', models.CharField(max_length=30)),
                ('jam', models.CharField(max_length=20)),
                ('hari', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.hari')),
            ],
        ),
        migrations.CreateModel(
            name='datamurid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('nohp', models.CharField(max_length=15)),
                ('alamat', models.CharField(max_length=225, null=True)),
                ('No_id', models.IntegerField()),
                ('kelamin', models.BooleanField(default=True)),
                ('pendidikan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.KtgAmpu')),
            ],
        ),
    ]
