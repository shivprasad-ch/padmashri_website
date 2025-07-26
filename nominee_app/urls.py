from django.urls import path
from . import views

urlpatterns = [
    # 🔹 Main Pages
    path('', views.home, name='home'),
    path('add-nominee/', views.add_nominee, name='add_nominee'),
    path('profiles/<int:pk>/', views.nominee_detail, name='nominee_detail'),
    path('download/zip/', views.download_all_zip, name='download_zip'),
    path('qr-code/<int:pk>/', views.generate_qr_code, name='qr_code'),

    # 🔹 Year-wise Views
    path('timeline/<int:year>/', views.timeline_by_year, name='timeline_by_year'),
    path('achievement/year/<int:year>/', views.achievement_by_year, name='achievement_by_year'),
    path('contribution/year/<int:year>/', views.contribution_by_year, name='contribution_by_year'),
    path('media/year/<int:year>/', views.media_by_year, name='media_by_year'),

    # 🔹 Detail Views
    path('achievement/<int:pk>/', views.achievement_detail, name='achievement_detail'),
    path('contribution/<int:pk>/', views.contribution_detail, name='contribution_detail'),
    path('media/<int:pk>/', views.media_detail, name='media_detail'),
    path('document/<int:pk>/', views.document_detail, name='document_detail'),

    # ✉️ Contact Form
    path('contact/', views.contact_form_view, name='contact_form'),  # ✅ Corrected view function name
]