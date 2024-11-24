from django.db import models

# Create your models here.
class Kamar(models.Model):
  nama = models.CharField(max_length=250)
  gambar = models.ImageField(upload_to="media/images")
  fasilitas = models.TextField()
  
  def __str__(self) -> str:
    return self.nama