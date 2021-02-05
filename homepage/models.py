from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField(max_length=100)
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return f'{self.title}|{self.author}|{self.instructions}'