
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from .models import (
    Nominee, Document, Achievement, MediaFile,
    Testimonial, Contribution, ContactRequest
)
from .forms import NomineeForm, ContactForm
import zipfile
from io import BytesIO

# 🏠 Homepage (One-Pager Layout)
def home(request):
    nominee = Nominee.objects.first()
    if not nominee:
        return HttpResponse("No nominee found. Please add a nominee from admin.")

    context = {
        'nominee': nominee,
        'achievements': Achievement.objects.filter(nominee=nominee),
        'media_files': MediaFile.objects.filter(nominee=nominee),
        'documents': Document.objects.filter(nominee=nominee),
        'testimonials': Testimonial.objects.filter(nominee=nominee),
        'contributions': Contribution.objects.filter(nominee=nominee),
        'contact': ContactRequest.objects.last(),  # ✅ Show latest contact info
    }
    return render(request, 'nominee_app/home.html', context)

# ➕ Add Nominee
def add_nominee(request):
    if request.method == 'POST':
        form = NomineeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'nominee_app/success.html')
    else:
        form = NomineeForm()
    return render(request, 'nominee_app/add_nominee.html', {'form': form})

# 👤 Nominee Profile View
def nominee_detail(request, pk):
    nominee = get_object_or_404(Nominee, pk=pk)
    context = {
        'nominee': nominee,
        'achievements': Achievement.objects.filter(nominee=nominee),
        'media_files': MediaFile.objects.filter(nominee=nominee),
        'documents': Document.objects.filter(nominee=nominee),
        'testimonials': Testimonial.objects.filter(nominee=nominee),
        'contributions': Contribution.objects.filter(nominee=nominee),
    }
    return render(request, 'nominee_app/nominee_detail.html', context)

# 📦 Download All Documents as ZIP
def download_all_zip(request):
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for doc in Document.objects.all():
            if doc.file and hasattr(doc.file, 'path'):
                try:
                    zip_file.write(doc.file.path, arcname=doc.file.name)
                except FileNotFoundError:
                    continue  # Skip missing files

    zip_buffer.seek(0)
    response = HttpResponse(zip_buffer, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="padma_nominee_docs.zip"'
    return response

# 🧾 QR Code Serve
def generate_qr_code(request, pk):
    nominee = get_object_or_404(Nominee, pk=pk)
    if nominee.qr_code and hasattr(nominee.qr_code, 'path'):
        return FileResponse(open(nominee.qr_code.path, 'rb'), content_type='image/png')
    return HttpResponse("QR code not available for this nominee.", status=404)

# 🔍 Detail Views
def contribution_detail(request, pk):
    contribution = get_object_or_404(Contribution, pk=pk)
    return render(request, 'contributions/detail.html', {'contribution': contribution})

def achievement_detail(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    return render(request, 'achievements/detail.html', {'achievement': achievement})

def media_detail(request, pk):
    media = get_object_or_404(MediaFile, pk=pk)
    return render(request, 'media/detail.html', {'media': media})

def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)
    return render(request, 'documents/detail.html', {'document': document})

# 📘 Views by Year
def timeline_by_year(request, year):
    contributions = Contribution.objects.filter(year=year)
    return render(request, 'detail_views/timeline_by_year.html', {
        'year': year,
        'contributions': contributions,
    })

def achievement_by_year(request, year):
    achievements = Achievement.objects.filter(year=year)
    return render(request, 'detail_views/achievements_by_year.html', {
        'year': year,
        'achievements': achievements,
    })

def contribution_by_year(request, year):
    contributions = Contribution.objects.filter(year=year)
    return render(request, 'detail_views/contributions_by_year.html', {
        'year': year,
        'contributions': contributions,
    })

def media_by_year(request, year):
    media_files = MediaFile.objects.filter(year=year)
    return render(request, 'detail_views/media_by_year.html', {
        'year': year,
        'media_files': media_files,
    })

# ✉️ Contact Form View
def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'nominee_app/contact_success.html')  # success message
    else:
        form = ContactForm()
    return render(request, 'nominee_app/contact_form.html', {'form': form}) 