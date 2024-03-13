from django.db import models

class Book(models.Model):
    name = models.CharField("Livro",max_length=200)
    author = models.CharField("Author",max_length=200)
    description = models.TextField("Description",max_length=400)
    gender = models.CharField("Gênero",max_length=100)
    image_url = models.CharField(max_length=400, blank=True, null=True)
    
    def __str__(self):
        return self.name