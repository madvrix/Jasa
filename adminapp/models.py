from django.db import models

PERTEMUAN=[('1X Pertemuan','1X Pertemuan'),('2X Pertemuan','2X Pertemuan'),('3X Pertemuan','3X Pertemuan'),('4X Pertemuan','4X Pertemuan')]
HARI=[('Senin','Senin'),('Selasa','Selasa'),('Rabu','Rabu'),('Kamis','Kamis'),('Jumat','Jumat'),('Sabtu','Sabtu'),('Minggu','Minggu')]
JAM=[('07-08 AM','07-08 AM'),('08-09 AM','08-09 AM'),('09-10 AM','09-10 AM'),('10-11 AM','10-11 AM'),('11-12 PM','11-12 PM')]

class KtgAmpu(models.Model):
    nama=models.CharField(max_length=10)

    def __str__(self):
        return self.nama

class paket(models.Model):
    no_pkt=models.IntegerField(null=True, blank=True)
    id_pkt=models.IntegerField(null=True)
    nama_pkt=models.CharField(max_length=200, null=True)
    jml_pertemuan=models.CharField(max_length=200,choices=PERTEMUAN,blank=True, null=True)
    biaya=models.IntegerField(null=True)

    hari_1=models.CharField(max_length=200,choices=HARI,blank=True)
    jam_1=models.CharField(max_length=200,choices=JAM,blank=True)

    hari_2=models.CharField(max_length=200,choices=HARI,blank=True)
    jam_2=models.CharField(max_length=200,choices=JAM,blank=True)

    hari_3=models.CharField(max_length=200,choices=HARI,blank=True)
    jam_3=models.CharField(max_length=200,choices=JAM,blank=True)

    hari_4=models.CharField(max_length=200,choices=HARI,blank=True)
    jam_4=models.CharField(max_length=200,choices=JAM,blank=True)

    def __str__(self):
        return self.nama_pkt


class dataguru(models.Model):
    KATEGORI_CHOICES = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )
    #id=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, primary_key=True)
    # norole=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE,null=True)
    #noid=models.IntegerField(blank=True,null=False)
    nama=models.CharField(max_length=30)
    nohp=models.CharField(max_length=15)
    alamat=models.CharField(max_length=225,null=True)
    biaya=models.IntegerField(blank=True,null=False)
    no_id=models.IntegerField()
    usia=models.IntegerField(blank=True,null=True)
    link=models.CharField(max_length=100, null=True)
    catatan=models.TextField(null=True)
    foto=models.ImageField(upload_to='img/')
    portofolio=models.FileField(upload_to='document/')
    gender=models.CharField(max_length=1, choices=KATEGORI_CHOICES,null=True)


    def __str__(self):
        return self.nama

class datamurid(models.Model):
    KATEGORI_CHOICES = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )
    #id=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, primary_key=True)
    # norole=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE,null=True)
    #noid=models.IntegerField(blank=True,null=False)
    nama=models.CharField(max_length=30)
    nohp=models.CharField(max_length=15)
    alamat=models.CharField(max_length=225,null=True)
    No_id=models.IntegerField()
    pendidikan=models.ForeignKey(KtgAmpu, on_delete=models.CASCADE, null=True)
    gender=models.CharField(max_length=1, choices=KATEGORI_CHOICES,null=True)

    def __str__(self):
        return self.nama
