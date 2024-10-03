from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomerUser(AbstractUser):
    ROLES = (
            ('admin', 'admin'),
            ('student', 'student'),
            ('teacher', 'teacher')
    )
    avatar = models.ImageField(upload_to='user_avatars/')
    phone_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=10, choices=ROLES, default='student')
    coins = models.IntegerField(default=0)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='student_group')

    def set_password(self, raw_password):
        super().set_password(raw_password)

    def __str__(self):
        return self.username

class Group(models.Model):
        DAYS = (
            ('Odd', 'Odd'),
            ('Even', 'Even'),
            ('Weekend', 'Weekend')
        )
        name = models.CharField(max_length=50)
        # members = models.ManyToManyField(CustomUser)
        teacher = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name='teacher')
        day = models.CharField(max_length=10, choices=DAYS)
        time = models.TimeField(default='09:00')
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        is_active = models.BooleanField(default=True)

        def __str__(self):
            return self.name