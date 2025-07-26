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
            qr_data = f"https://yourdomain.com/profiles/{self.id}/"  # Replace with actual URL
            qr = qrcode.make(qr_data)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            file_name = f'qr_{self.full_name.replace(" ", "_")}.png'
            self.qr_code.save(file_name, File(buffer), save=False)
        super().save(*args, **kwargs)


# 📅 Year-wise Contributions
class Contribution(models.Model):
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.nominee.full_name} - {self.year} - {self.title}"


# 🏅 Awards and Recognitions
class Achievement(models.Model):
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  # <-- renamed from 'award_name'
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.year})"


# 📸 Media Files (Photos/Videos)
class MediaFile(models.Model):
    MEDIA_TYPES = (
        ('photo', 'Photo'),
        ('video', 'Video'),
    )
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return f"{self.file_type.capitalize()} - {self.nominee.full_name}"


# 📄 Supporting Documents
class Document(models.Model):
    DOC_TYPES = (
        ('dossier', 'Dossier'),
        ('resume', 'Resume/Biodata'),
        ('recommendation', 'Letter of Recommendation'),
        ('news', 'News Article'),
        ('id', 'ID Proof'),
    )
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=20, choices=DOC_TYPES)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return f"{self.doc_type.capitalize()} - {self.nominee.full_name}"


# 💬 Testimonials from Others
class Testimonial(models.Model):
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=100)
    quote = models.TextField()
    video = models.FileField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return f"{self.person_name} on {self.nominee.full_name}"


# 📬 Contact Form Submissions
class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
