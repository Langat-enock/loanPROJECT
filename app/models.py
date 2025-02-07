from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class LoanApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]

    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True,max_length=15)
    loan_id = models.CharField(max_length=20, unique=True)
    identification_id = models.CharField(max_length=50, unique=True)
    loan_security = models.FileField(upload_to='loan_security_documents/')
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    credit_score = models.IntegerField()
    purpose = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def approve(self):
        """Method to approve loan"""
        self.status = 'approved'
        self.save()

    def reject(self):
        """Method to reject loan"""
        self.status = 'rejected'
        self.save()

    def __str__(self):
        return f"Loan Application {self.loan_id} - {self.status}"

    class Meta:
        db_table = 'loan_application'

#         run the migration  command
#         python manage.py makemigrations
#          python manage.py migrate


