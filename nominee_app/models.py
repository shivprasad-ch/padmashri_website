from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

# 🧑‍🏫 Main Nominee Profile
class Nominee(models.Model):
    full_name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to='photos/')
    bio = models.TextField()
    field_of_work = models.CharField(max_length=100)
    impact_numbers = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.qr_code:
            qr_data = f"https://yourdomain.com/profiles/{self.id}/"
            qr = qrcode.make(qr_data)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            file_name = f'qr_{self.full_name.replace(" ", "_")}.png'
            self.qr_code.save(file_name, File(buffer), save=False)
        super().save(*args, **kwargs)

# 🔸 Subpoints
class ContributionSubpoint(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class AchievementSubpoint(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class DocumentSubpoint(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class MediaSubpoint(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class TestimonialSubpoint(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

# 🔹 Linked Data Models
class Contribution(models.Model):
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    subpoint = models.ForeignKey(ContributionSubpoint, on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.year} - {self.title}"

class Achievement(models.Model):
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    subpoint = models.ForeignKey(AchievementSubpoint, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

class Document(models.Model):
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    subpoint = models.ForeignKey(DocumentSubpoint, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return f"{self.doc_type}"

class MediaFile(models.Model):
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    subpoint = models.ForeignKey(MediaSubpoint, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10, choices=(('photo', 'Photo'), ('video', 'Video')))
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return f"{self.file_type}"

class Testimonial(models.Model):
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    subpoint = models.ForeignKey(TestimonialSubpoint, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=100)
    quote = models.TextField()
    video = models.FileField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.person_name

# 📬 Contact Form Submissions
class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"