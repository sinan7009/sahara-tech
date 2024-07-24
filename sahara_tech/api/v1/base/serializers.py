from rest_framework import serializers
from base.models import Logo, Navbar, MainHeading, Consultation, TechHeading, TechSlider, Vedio, MainSlider, \
    CustomersHeading, Client, NewsHeading, NewsSlider, Community


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['logo_url', 'logo_img', 'company_name','id', ]


class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = ('id', 'navbar_name')


class MainHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainHeading
        fields = ['highlighted_text', 'text', 'id']


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['name', 'email', 'country', 'phone', 'query', 'id']


class TechHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechHeading
        fields = ['highlighted_text', 'text', 'side_heading', 'id']


class TechSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechSlider
        fields = ['tech_notes', 'tech_logo_url', 'tech_logo_img', 'id']


class VedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vedio
        fields = ['video_url', 'video_file', 'video_title', 'id']


class MainSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = ['index_no', 'index_title', 'slider_note', 'title', 'paragraph', 'id']


class CustomerHeadingSerailizer(serializers.ModelSerializer):
    class Meta:
        model = CustomersHeading
        fields = ['text', 'side_heading', 'image_url', 'image', 'paragraph', 'id']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['logo_url', 'logo_img', 'id']


class NewsHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsHeading
        fields = ['heading', 'side_heading', 'id']


class NewsSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSlider
        fields = ['slider_heading', 'slider_paragraph', 'id']


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['email_label', 'community_email', 'id']
