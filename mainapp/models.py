
from django.db import models
from django.utils.text import slugify


# ======================================================
# Base / Abstract Models
# ======================================================

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ======================================================
# Core Website Models
# ======================================================

class HeroSection(TimeStampedModel):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    primary_button_text = models.CharField(max_length=50, blank=True)
    primary_button_link = models.URLField(blank=True)

    secondary_button_text = models.CharField(max_length=50, blank=True)
    secondary_button_link = models.URLField(blank=True)

    hero_image = models.ImageField(upload_to="hero/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class AboutSection(TimeStampedModel):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="about/")
    years_of_experience = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.heading


# class Feature(TimeStampedModel):
#     title = models.CharField(max_length=150)
#     description = models.TextField()
#     icon = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.title


class Service(TimeStampedModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Stacks(TimeStampedModel):
    name = models.CharField(max_length=100)
    stats = models.PositiveIntegerField(default=0)
    logo = models.ImageField(upload_to="technologies/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# ======================================================
# Business & Trust Models
# ======================================================

# class Counter(TimeStampedModel):
#     label = models.CharField(max_length=100)
#     count = models.PositiveIntegerField()
#     icon = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.label


# class Testimonial(TimeStampedModel):
#     client_name = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100, blank=True)
#     company = models.CharField(max_length=100, blank=True)
#     message = models.TextField()
#     profile_image = models.ImageField(upload_to="testimonials/", blank=True)
#     rating = models.PositiveSmallIntegerField(default=5)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.client_name


class Partner(TimeStampedModel):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="partners/")
    website = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# ======================================================
# Team & Company Models
# ======================================================

class TeamMember(TimeStampedModel):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="team/")
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CompanyInfo(TimeStampedModel):
    company_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.TextField()
    map_embed_url = models.TextField(blank=True)

    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return self.company_name


# ======================================================
# Blog Models
# ======================================================

# class BlogCategory(TimeStampedModel):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True, blank=True)
#     is_active = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.name


# class BlogPost(TimeStampedModel):
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True, blank=True)
#     category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
#     short_description = models.CharField(max_length=255)
#     content = models.TextField()
#     featured_image = models.ImageField(upload_to="blogs/")
#     author = models.CharField(max_length=100)
#     published_date = models.DateField()
#     is_published = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.title


# ======================================================
# Contact & Interaction Models
# ======================================================

class ContactMessage(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"


# class NewsletterSubscriber(TimeStampedModel):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.email


# class QuoteRequest(TimeStampedModel):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
#     message = models.TextField()

#     def __str__(self):
#         return self.name


# ======================================================
# Footer, SEO & Utility Models
# ======================================================

class FooterLink(TimeStampedModel):
    ICON_CHOICES = [
        ('twitter-x', 'Twitter / X'),
        ('facebook',  'Facebook'),
        ('instagram', 'Instagram'),
        ('linkedin',  'LinkedIn'),
        ('youtube',   'YouTube'),
        ('tiktok',    'TikTok'),
    ]
    title = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=20, choices=ICON_CHOICES)
    section_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class SEOSettings(TimeStampedModel):
    page_name = models.CharField(max_length=100, unique=True)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=300)

    def __str__(self):
        return self.page_name


class PageBanner(TimeStampedModel):
    page_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    background_image = models.ImageField(upload_to="banners/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.page_name


class FAQ(TimeStampedModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question

    
