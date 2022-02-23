from django.shortcuts import render

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins

from .models import *
from .serializer import *

#######################SLA#########################
def SLHome(request):
    return render(request,'ServiceAgreement/home.html')


class SLAList(APIView):
    def get(self,request):
         queryset               =         SLA.objects.all()
         serializer             =         SLASerializer(queryset,many=True)
         permission_classes     =         []
         authentication_class   =         []
         return Response (serializer.data)

    def post(self,request):
            serializer           =         SLASerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SLAdetail(APIView):

class SLADetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset                = SLA.objects.all()
    serializer_class        = SLASerializer
    permission_classes      = []
    # authentication_classes  = [SessionAuthentication]
    lookup_field            = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





###########################History##############################

class HistoryList(APIView):
    def get(self,request):
        History_queryset       =        History.objects.all()
        serializers_class      =        HistorySerializer(History_queryset,many=True)
        permission_classes     =         []
        authentication_class   =         []
        return Response(serializers_class.data)

    def post(self,request):
            serializer           =         HistorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
# class HistoryUpdateAPIView(generics.UpdateAPIView):
#     queryset               =       History.objects.all()
#     serializers_class      =       HistorySerializer
#     permission_classes     =         []
#     authentication_class   =         []
#     lookup_field           =         'pk'

#
# def sla(request):
#     return render(request,'sla/dashboard.html')


