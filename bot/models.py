from django.db import models

# Create your models here.


class Subject(models.Model):

    DIFFICULTY_CHOICES = [("easy", "easy"), ("medium", "medium"), ("hard", "hard")]

    name = models.CharField(max_length=200, unique=True)
    difficulity = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subject"


class Document(models.Model):
    url = models.URLField()
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="documents"
    )

    def __str__(self):
        return self.url

    class Meta:
        db_table = "DOCUMENTS"
    
class Book(models.Model):
    Dept = models.CharField(max_length=80)
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=80,null=True)
    Location = models.CharField(max_length = 10,null=True)

    def __str__(self):
        return self.Title
    
    class Meta:
        db_table = "BOOKS"

class PQP(models.Model):
    Regulation = models.CharField(max_length=10)
    Semester = models.CharField(max_length=10)
    Branch = models.CharField(max_length=10)
    Subject = models.CharField(max_length=100,null=True)
    Year = models.CharField(max_length=15,null=True)
    Link = models.URLField()

    def __str__(self):
        return self.Regulation
    
    class Meta:
        db_table = "PQP"

class PPT(models.Model):
    Regulation = models.CharField(max_length=10)
    Semester = models.CharField(max_length=10)
    Branch = models.CharField(max_length=10)
    Subject = models.CharField(max_length=100,null=True)
    Year = models.CharField(max_length=15,null=True)
    Link = models.URLField()

    def __str__(self):
        return self.Regulation
    
    class Meta:
        db_table = "PPT"