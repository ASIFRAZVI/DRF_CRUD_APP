from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import crudobj
from .serializers import *

class Crud_Application(APIView):
    def post(self, request):
        data=request.data
        serializer=crud_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"ceared"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,  request):
        data=crudobj.objects.all()
        print(data)
        serializer=crud_serializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        try:
            instance=crudobj.objects.get(pk=pk)
        except:
            return Response({"message":"pk not found"},status=status.HTTP_404_NOT_FOUND)
        serializer=crud_serializer(instance , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            instance = crudobj.objects.get(pk=pk)
        except crudobj.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


    
