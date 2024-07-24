from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/base/update/<int:pk>/',BaseUpdateDeleteView.as_view(),name ='update_view'),
    path('api/v1/base/logo/',LogoView.as_view(),name = 'log_view'),
    path('api/v1/base/logo/<int:pk>/',LogoViews.as_view(),name = 'log_views'),
    path('api/v1/base/navbar/',NavbarView.as_view(), name='Navbar_view'),
    path('api/v1/base/navbar/<int:pk>/',NavbarViews.as_view(), name='Navbar_views'),
    path('api/v1/base/mainheading/',MainHeadingView.as_view(), name='Mainheading_view'),
    path('api/v1/base/mainheading/<int:pk>/',MainHeadingViews.as_view(), name='Mainheading_views'),
    path('api/v1/base/consultation/',ConsultaionView.as_view(), name='consultation_view'),
    path('api/v1/base/consultation/<int:pk>/',ConsultationViews.as_view(), name='Consultation_views'),
    path('api/v1/base/techheading/',TechHeadingView.as_view(), name='techheading_view'),
    path('api/v1/base/techheading/<int:pk>/',TechHeadingViews.as_view(), name='techheading_views'),
    path('api/v1/base/techslider/',TechSliderView.as_view(), name='techslider_view'),
    path('api/v1/base/techslider/<int:pk>/',TechSliderViews.as_view(), name='techslider_views'),
    path('api/v1/base/video/',VedioView.as_view(), name='vedio_view'),
    path('api/v1/base/video/<int:pk>/',VedioViews.as_view(), name='vedio_views'),
    path('api/v1/base/mainslider/', MainSliderView.as_view(), name='mainslider_view'),
    path('api/v1/base/mainslider/<int:pk>/', MainSliderViews.as_view(), name='mainslider_views'),
    path('api/v1/base/customerheading/',CustomerHeadingView.as_view(), name='customerheading_view'),
    path('api/v1/base/customerheading/<int:pk>/', CustomerHeadingViews.as_view(), name='customerheading_views'),
    path('api/v1/base/client/',ClientView.as_view(), name='client_view'),
    path('api/v1/base/client/<int:pk>/', ClientViews.as_view(), name='client_views'),
    path('api/v1/base/newsheading/',NewsHeadingView.as_view(), name='newsheading_view'),
    path('api/v1/base/newsheading/<int:pk>/', NewsHeadingViews.as_view(), name='newsheading_views'),
    path('api/v1/base/newsslider/',NewsSliderView.as_view(), name='newslider_view'),
    path('api/v1/base/newsslider/<int:pk>/', NewsSliderViews.as_view(), name='newsslider_views'),
    path('api/v1/base/community/',CommunityView.as_view(), name='community_view'),
    path('api/v1/base/community/<int:pk>/', CommunityViews.as_view(), name='community_views'),

]
