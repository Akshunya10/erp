from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    return render(request,'crm/home.html')

def about(request):
    return render(request,'crm/about.html')

def contact(request):
    return render(request,'crm/contact.html')




# from django.contrib.auth.decorators import login_required


# @login_required
# def home(request):
#     return render(request,'base.html',{})


# from django.views.generic import TemplateView


# class HomePageView(TemplateView):
#     template_name = 'home.html'



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User

# class ListUsers(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     permission_classes = [permissions.IsAdminUser]

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)