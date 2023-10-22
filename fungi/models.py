from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name
    
class Fungi(models.Model):
    EDIBILITY_CHOICES = [
        ('COM', 'Comestible'),
        ('COO', 'Cooked Only'),
        ('NI', 'Not Interesting'),
        ('TOX', 'Toxic'),
        ('MOR', 'Mortal'),
    ]
    french_name = models.CharField(max_length=200)
    latin_name = models.CharField(max_length=200)
    edibility = models.CharField(max_length=3, choices=EDIBILITY_CHOICES, default='NI')
    smell = models.TextField(blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.latin_name

class FungiImage(models.Model):
    fungi = models.ForeignKey(Fungi, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='fungi_images/')

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    total_questions = models.PositiveIntegerField(default=20)
    date_taken = models.DateTimeField(auto_now_add=True)

