from django.contrib import admin
from .models import (
    Nominee, Contribution, Achievement,
    Document, MediaFile, Testimonial, ContactRequest
)

# 🔹 Inline Models (Editable from Nominee Admin)
class ContributionInline(admin.TabularInline):
    model = Contribution
    extra = 1

class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 1

class MediaFileInline(admin.TabularInline):
    model = MediaFile
    extra = 1

class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1

class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 1

# 🔸 Nominee Admin with Inlines
@admin.register(Nominee)
class NomineeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'field_of_work', 'last_updated')
    list_display_links = ('full_name',)
    search_fields = ('full_name', 'field_of_work')
    list_filter = ('field_of_work',)
    inlines = [
        ContributionInline,
        AchievementInline,
        MediaFileInline,
        DocumentInline,
        TestimonialInline
    ]

# 🔸 Contribution Admin
@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('nominee', 'year', 'title')
    list_display_links = ('title',)
    list_filter = ('year',)
    search_fields = ('nominee__full_name', 'title', 'description')

# 🔸 Achievement Admin
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('nominee', 'title', 'year')
    list_display_links = ('title',)
    list_filter = ('year',)
    search_fields = ('title', 'nominee__full_name')

# 🔸 Document Admin
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('nominee', 'doc_type')
    list_display_links = ('doc_type',)
    list_filter = ('doc_type',)
    search_fields = ('nominee__full_name',)

# 🔸 Media File Admin
@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('nominee', 'file_type')
    list_display_links = ('file_type',)
    list_filter = ('file_type',)
    search_fields = ('nominee__full_name',)

# 🔸 Testimonial Admin
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'nominee')
    list_display_links = ('person_name',)
    search_fields = ('person_name', 'nominee__full_name')

# 🔸 Contact Request Admin (fixed: now editable)
@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')