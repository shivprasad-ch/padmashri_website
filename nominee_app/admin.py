from django.contrib import admin
from .models import (
    Nominee, Contribution, Achievement, Document, MediaFile, Testimonial,
    ContributionSubpoint, AchievementSubpoint, DocumentSubpoint, MediaSubpoint, TestimonialSubpoint,
    ContactRequest
)

# 🔹 Inline Models for quick add/edit under Nominee
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

# 🔸 Nominee Admin with inlines
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
        TestimonialInline,
    ]

# 🔹 Contribution Admin
@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('nominee', 'subpoint', 'year', 'title')
    list_filter = ('year', 'subpoint')
    search_fields = ('nominee__full_name', 'title', 'description')

# 🔹 Achievement Admin
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('nominee', 'subpoint', 'title', 'year')
    list_filter = ('year', 'subpoint')
    search_fields = ('title', 'nominee__full_name')

# 🔹 Document Admin
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('nominee', 'subpoint', 'doc_type')
    list_filter = ('doc_type', 'subpoint')
    search_fields = ('nominee__full_name',)

# 🔹 Media Admin
@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('nominee', 'subpoint', 'file_type')
    list_filter = ('file_type', 'subpoint')
    search_fields = ('nominee__full_name',)

# 🔹 Testimonial Admin
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'nominee', 'subpoint')
    list_filter = ('subpoint',)
    search_fields = ('person_name', 'nominee__full_name')

# 🔹 Contact Admin
@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')


# 🔸 Subpoint Model Registrations
admin.site.register(ContributionSubpoint)
admin.site.register(AchievementSubpoint)
admin.site.register(DocumentSubpoint)
admin.site.register(MediaSubpoint)
admin.site.register(TestimonialSubpoint)