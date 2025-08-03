from django.db import models
from django.utils import timezone

class Applicant(models.Model):
    POSITION_CHOICES = [
        ('intern', 'Intern'),
        ('volunteer', 'Volunteer'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    
    # Application Details
    position_type = models.CharField(max_length=20, choices=POSITION_CHOICES)
    department = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    # Education & Experience
    current_education = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    graduation_year = models.IntegerField()
    relevant_experience = models.TextField()
    
    # Motivation & Skills
    motivation = models.TextField()
    skills = models.TextField()
    
    # Additional Information
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    cover_letter = models.TextField(blank=True)
    
    # Application Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_date = models.DateTimeField(default=timezone.now)
    admin_notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position_type}"
    
    class Meta:
        ordering = ['-applied_date']
