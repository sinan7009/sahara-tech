from django.db import models
from django.utils.translation import gettext_lazy as _


class Logo(models.Model):
    logo_url = models.URLField(null=True, blank=True)
    logo_img = models.ImageField(null=True, blank=True)
    company_name = models.CharField(max_length=64, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_logo'
        verbose_name = _('logo')
        verbose_name_plural = _('logos')
        ordering = ('company_name',)


class Navbar(models.Model):
    navbar_name = models.SlugField(max_length=32, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_navbar'
        verbose_name = _('navbar')
        verbose_name_plural = _('navbar')
        ordering = ('navbar_name',)

    def _str_(self):
        return self.navbar_name


class MainHeading(models.Model):
    highlighted_text = models.CharField(max_length=128, null=True, blank=True)
    text = models.CharField(max_length=128, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_mainHeading'
        verbose_name = _('mainHeading')
        verbose_name_plural = _('mainHeadings')
        ordering = ('text',)


class Consultation(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    query = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'base_consultation'
        verbose_name = _('consultation')
        verbose_name_plural = _('consultations')
        ordering = ('name',)

    def _str_(self):
        return self.name


class TechHeading(models.Model):
    text = models.CharField(max_length=128, null=True, blank=True)
    highlighted_text = models.CharField(max_length=128, null=True, blank=True)
    side_heading = models.CharField(max_length=32, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_techHeading'
        verbose_name = _('techHeading')
        verbose_name_plural = _('techHeadings')
        ordering = ('text',)


class TechSlider(models.Model):
    tech_notes = models.TextField(null=True, blank=True)
    tech_logo_url = models.URLField(max_length=256, null=True, blank=True)
    tech_logo_img = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_techSlider'
        verbose_name = _('techSlider')
        verbose_name_plural = _('techSliders')
        ordering = ('tech_notes',)


class Vedio(models.Model):
    video_url = models.URLField(null=True, blank=True)
    video_file = models.FileField(null=True, blank=True)
    video_title = models.CharField(max_length=64, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, )
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_video'
        verbose_name = _('video')
        verbose_name_plural = _('videos')
        ordering = ('video_title',)


class MainSlider(models.Model):
    index_no = models.IntegerField(null=True, blank=True)
    index_title = models.CharField(max_length=64, null=True, blank=True)
    slider_note = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    paragraph = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_mainSlider'
        verbose_name = _('mainSlider')
        verbose_name_plural = _('videos')
        ordering = ('index_title',)


class CustomersHeading(models.Model):
    text = models.CharField(max_length=62, null=True, blank=True)
    side_heading = models.CharField(max_length=32, null=True, blank=True)
    image_url = models.URLField(max_length=256, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    paragraph = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_customersHeading'
        verbose_name = _('customersHeading')
        verbose_name_plural = _('customersHeadings')
        ordering = ('side_heading',)


class Client(models.Model):
    logo_url = models.URLField(max_length=256, null=True, blank=True)
    logo_img = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_client'
        verbose_name = _('client')
        verbose_name_plural = _('clients')
        ordering = ('logo_url',)


class NewsHeading(models.Model):
    heading = models.CharField(max_length=128, null=True, blank=True)
    side_heading = models.CharField(max_length=32, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_newsHeading'
        verbose_name = _('newsHeading')
        verbose_name_plural = _('newsHeadings')
        ordering = ('side_heading',)


class NewsSlider(models.Model):
    slider_heading = models.CharField(max_length=64, null=True, blank=True)
    slider_paragraph = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_newsSlider'
        verbose_name = _('newsSlider')
        verbose_name_plural = _('newsSliders')
        ordering = ('slider_heading',)


class Community(models.Model):
    email_label = models.CharField(max_length=64, null=True, blank=True)
    community_email = models.EmailField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'base_community'
        verbose_name = _('community')
        verbose_name_plural = _('communities')
        ordering = ('email_label',)
