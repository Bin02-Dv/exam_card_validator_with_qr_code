from django.db import models

# Create your models here.

class Exam(models.Model):
    exam_regis = models.CharField(max_length=10, unique=True)
    exam_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Student Registration Number - {self.exam_regis}"

class QRCode(models.Model):
    code_image = models.ImageField(upload_to='qr_codes/')
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return f"Exam - {self.exam}"

