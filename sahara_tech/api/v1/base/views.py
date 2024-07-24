from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from base.models import *


class BaseUpdateDeleteView(APIView):
    serializer_class = None
    model = None

    def get_record(self, request, pk):
        try:
            object = self.model.objects.get(pk=pk)
            serializer = self.serializer_class(object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_records(self, request):
        try:
            object = self.model.objects.all()
            serailizer = self.serializer_class(object, many=True, context={'request': request})
            return Response({
                'status': 'listed',
                'data': serailizer.data
            },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post_record(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status': 'bad request', 'error': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'status': 'not created', 'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put_record(self, request, pk):
        try:
            object = self.model.objects.get(pk=pk)
        except Logo.DoesNotExist:
            return Response({'status': 'not found', 'error': 'not found '},
                            status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = self.serializer_class(object, data=request.data, partial=False, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'updated', 'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status': 'bad request', 'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'status': "not updated", 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch_record(self, request, pk):
        try:
            object = self.model.objects.get(pk=pk)
        except Logo.DoesNotExist:
            return Response({'status': 'not found', 'error': 'not found '},
                            status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = self.serializer_class(object, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'updated', 'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status': 'bad request', 'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'status': "not updated", 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete_record(self, request, pk):
        try:
            object = self.model.objects.get(pk=pk)
            object.delete()
            return Response({'status': 'deleted', 'message': 'deleted succesfully'},
                            status=status.HTTP_200_OK)

        except object.DoesNotExist:
            return Response({'status': 'logo not found', 'errors': 'logo not found'},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': 'not deleted', 'errors': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogoView(BaseUpdateDeleteView):
    serializer_class = LogoSerializer
    model = Logo

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class LogoViews(BaseUpdateDeleteView):
    serializer_class = LogoSerializer
    model = Logo

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class NavbarView(BaseUpdateDeleteView):
    serializer_class = NavbarSerializer
    model = Navbar

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class NavbarViews(BaseUpdateDeleteView):
    serializer_class = NavbarSerializer
    model = Navbar

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class MainHeadingView(BaseUpdateDeleteView):
    serializer_class = MainHeadingSerializer
    model = MainHeading

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class MainHeadingViews(BaseUpdateDeleteView):
    serializer_class = MainHeadingSerializer
    model = MainHeading

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class ConsultaionView(BaseUpdateDeleteView):
    serializer_class = ConsultationSerializer
    model = Consultation

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class ConsultationViews(BaseUpdateDeleteView):
    serializer_class = ConsultationSerializer
    model = Consultation

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class TechHeadingView(BaseUpdateDeleteView):
    serializer_class = TechHeadingSerializer
    model = TechHeading

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class TechHeadingViews(BaseUpdateDeleteView):
    serializer_class = TechHeadingSerializer
    model = TechHeading

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class TechSliderView(BaseUpdateDeleteView):
    serializer_class = TechSliderSerializer
    model = TechSlider

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class TechSliderViews(BaseUpdateDeleteView):
    serializer_class = TechSliderSerializer
    model = TechSlider

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class VedioView(BaseUpdateDeleteView):
    serializer_class = VedioSerializer
    model = Vedio

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class VedioViews(BaseUpdateDeleteView):
    serializer_class = VedioSerializer
    model = Vedio

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class MainSliderView(BaseUpdateDeleteView):
    serializer_class = MainSliderSerializer
    model = MainSlider

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class MainSliderViews(BaseUpdateDeleteView):
    serializer_class = MainSliderSerializer
    model = MainSlider

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class CustomerHeadingView(BaseUpdateDeleteView):
    serializer_class = CustomerHeadingSerailizer
    model = CustomersHeading

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class CustomerHeadingViews(BaseUpdateDeleteView):
    serializer_class = CustomerHeadingSerailizer
    model = CustomersHeading

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class ClientView(BaseUpdateDeleteView):
    serializer_class = ClientSerializer
    model = Client

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class ClientViews(BaseUpdateDeleteView):
    serializer_class = ClientSerializer
    model = Client

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class NewsHeadingView(BaseUpdateDeleteView):
    serializer_class = NewsHeadingSerializer
    model = NewsHeading

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class NewsHeadingViews(BaseUpdateDeleteView):
    serializer_class = NewsHeadingSerializer
    model = NewsHeading

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class NewsSliderView(BaseUpdateDeleteView):
    serializer_class = NewsSliderSerializer
    model = NewsSlider

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class NewsSliderViews(BaseUpdateDeleteView):
    serializer_class = NewsSliderSerializer
    model = NewsSlider

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)


class CommunityView(BaseUpdateDeleteView):
    serializer_class = CommunitySerializer
    model = Community

    def get(self, request):
        return self.get_records(request)

    def post(self, request):
        return self.post_record(request)


class CommunityViews(BaseUpdateDeleteView):
    serializer_class = CommunitySerializer
    model = Community

    def get(self, request, pk):
        if pk:
            return self.get_record(request, pk)

    def put(self, request, pk):
        return self.put_record(request, pk)

    def patch(self, request, pk):
        return self.patch_record(request, pk)

    def delete(self, request, pk):
        return self.delete_record(request, pk)
