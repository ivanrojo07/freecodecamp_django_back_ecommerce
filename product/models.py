from django.db import models
from django.core.files import File

from PIL import Image
from io import BytesIO

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=255)
    slug= models.SlugField()

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True,upload_to='uploads/')
    thumbnail = models.ImageField(blank=True,null=True,upload_to="uploads/")
    slug = models.SlugField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    date_added= models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000'+self.image.url
        else:
            return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000'+self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000'+self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self,image, size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()

        img.save(thumb_io,'JPEG',quality=85)

        thumbnail = File(thumb_io,name=image.name)

        return thumbnail
