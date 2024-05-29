from django.shortcuts import render

# Create your views here.
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status

from s3.settings import AWS_STORAGE_BUCKET_NAME
import boto3
class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request):
        file_obj = request.data['file']
        # Save the file to the model or directly upload it to S3
        # You can use the Boto3 library to upload the file to S3.
        #For example:
        s3_client = boto3.client('s3')
        s3_client.upload_fileobj(file_obj, AWS_STORAGE_BUCKET_NAME, file_obj.name)
        
        # Return a success response or handle errors accordingly
        return Response({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)
