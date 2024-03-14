from django.db import models
# Create your models here.
# Un Job est caractérisé par: 

# - id 
# - reference 
# - titre 
# - description 
# - image 
# - file 
# - salaire 
# - status (open, pending, close)
# - publish_date 
# - close_date 

class Job(models.Model):

    STATUS = (
        ('O', 'OPENED'),
        ('P', 'PENDING'),
        ('C','CLOSED')
    )

    referene = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default='default.jpg')
    file = models.FileField(upload_to="uploads/")
    salaire = models.PositiveIntegerField(default=100000)
    status = models.CharField(max_length=1, choices=STATUS, default="O")
    publish_date = models.DateTimeField(auto_now=True)
    closed_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'jobs'
        ordering = ['-created_at']
        verbose_name = 'Job'
        verbose_name_plural = "jobs"


