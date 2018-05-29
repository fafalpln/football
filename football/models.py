from django.db import models
from django.utils import timezone


class Druzyna(models.Model):
    nazwa=models.CharField(max_length=30)
    stadion=models.CharField(max_length=30)
    miasto=models.CharField(max_length=30)

class Zawodnik(models.Model):
    imie=models.CharField(max_length=20)
    nazwisko=models.CharField(max_length=30)
    pozycja=models.CharField(max_length=10)
    data_urodzenia=models.DateField()
    narodowosc=models.CharField(max_length=20)

class Klasyfikacja(models.Model):
    id_druzyny=models.ForeignKey(Druzyna, on_delete=models.CASCADE)
    mecze=models.IntegerField(default=0)
    zwyciestwa=models.IntegerField(default=0)
    remisy=models.IntegerField(default=0)
    porazki=models.IntegerField(default=0)
    bramki_stracone=models.IntegerField(default=0)
    bramki_strzelone=models.IntegerField(default=0)
    punkty=models.IntegerField(default=0)

class Druzyna_Zawodnik(models.Model):
    id_druzyny=models.ForeignKey(Druzyna, on_delete=models.CASCADE)
    id_zawodnika=models.ForeignKey(Zawodnik, on_delete=models.CASCADE)
    nr_koszulki=models.IntegerField

class Strzelec(models.Model):
    id_zawodnika=models.ForeignKey(Zawodnik, on_delete=models.CASCADE)
    bramki=models.IntegerField(default=0)
    asysty=models.IntegerField(default=0)

class Mecz(models.Model):
    data=models.DateField()
    bramki_1=models.IntegerField(default=0)
    bramki_2=models.IntegerField(default=0)
    nr_kolejki=models.IntegerField()

class Mecz_Druzyna(models.Model):
    id_meczu=models.ForeignKey(Mecz, on_delete=models.CASCADE)
    id_druzyny=models.ForeignKey(Druzyna, on_delete=models.CASCADE)


class Statystyka(models.Model):
    id_meczu=models.ForeignKey(Mecz, on_delete=models.CASCADE)
    id_zawodnika=models.ForeignKey(Zawodnik, on_delete=models.CASCADE)
    bramki=models.IntegerField(default=0)
    asysty=models.IntegerField(default=0)
    kartka_czerwona=models.IntegerField(default=0)
    kartka_zolta=models.IntegerField(default=0)

# Create your models here.
