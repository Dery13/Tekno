from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Menus(models.Model):
    menu = models.CharField(max_length=100, blank=True, null=False)
    harga = models.CharField(max_length=100, blank=False, null=False)
    deskripsi = RichTextUploadingField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='media/menu/', blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.menu, self.harga)
    
    def ImgUrl(self):
        if self.thumbnail == '' or self.thumbnail == None

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Menus"

# Create your models here.
