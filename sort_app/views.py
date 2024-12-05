from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from rest_framework.views import APIView


class SortArrayAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data if request.data else None
            if data:
                # print(f"\n Request - {data}")
                
                # Bubble sort implementation
                sorted_data = data.copy()
                n = len(sorted_data)
                for i in range(n - 1):
                    for j in range(n - i - 1):
                        if sorted_data[j]['phone'] > sorted_data[j + 1]['phone']:
                            sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
                

                return Response({
                "message":"No data found.",
                "status":HTTP_400_BAD_REQUEST,
                "data":sorted_data,
            })
            # input_data = request.data
            return Response({
                "message":"sorted succesfully.",
                "status":HTTP_400_BAD_REQUEST,
            
            })
        except Exception as e:
            return Response({
                "message":"Something went wrong.",
                "status":HTTP_500_INTERNAL_SERVER_ERROR,
            
            })
