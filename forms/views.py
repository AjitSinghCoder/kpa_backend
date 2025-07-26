from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer
from utils.response import CustomResponse
custom_response = CustomResponse()


class WheelSpecificationList(APIView):
    @swagger_auto_schema(
        operation_description="Get list of wheel specifications with optional filtering",
        manual_parameters=[
            openapi.Parameter('formNumber', openapi.IN_QUERY, description="Filter by form number", type=openapi.TYPE_STRING),
            openapi.Parameter('submittedBy', openapi.IN_QUERY, description="Filter by submitted by", type=openapi.TYPE_STRING),
            openapi.Parameter('submittedDate', openapi.IN_QUERY, description="Filter by submitted date (YYYY-MM-DD)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
            openapi.Parameter('page', openapi.IN_QUERY, description="Page number", type=openapi.TYPE_INTEGER),
        ],
        responses={
            200: openapi.Response(
                description="Wheel specification list fetched successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "data": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "formNumber": openapi.Schema(type=openapi.TYPE_STRING),
                                    "submittedBy": openapi.Schema(type=openapi.TYPE_STRING),
                                    "submittedDate": openapi.Schema(type=openapi.TYPE_STRING),
                                    "fields": openapi.Schema(type=openapi.TYPE_STRING),
                                }
                            )
                        ),
                        "message": openapi.Schema(type=openapi.TYPE_STRING),
                        "success": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        "count": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "next": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI),
                        "previous": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI),
                    }
                )
            )
        }
    )
    def get(self, request):
        formNumber = request.query_params.get('formNumber')
        submittedBy = request.query_params.get('submittedBy')
        submittedDate = request.query_params.get('submittedDate')

        queryset = WheelSpecification.objects.all()

        if formNumber:
            queryset = queryset.filter(formNumber=formNumber)
        if submittedBy:
            queryset = queryset.filter(submittedBy=submittedBy)
        if submittedDate:
            queryset = queryset.filter(submittedDate=submittedDate)

        # Pagination
        paginator = PageNumberPagination()
        paginated_qs = paginator.paginate_queryset(queryset, request)
        serializer = WheelSpecificationSerializer(paginated_qs, many=True)

        return paginator.get_paginated_response({
            "data": serializer.data,
            "message": "Filtered wheel specification forms fetched successfully.",
            "success": True,
        })



class WheelSpecificationCreate(APIView):
    @swagger_auto_schema(
        operation_description="Create a new wheel specification",
        request_body=WheelSpecificationSerializer,
        responses={
            201: openapi.Response(
            description="Wheel specification created successfully",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                            "formNumber": openapi.Schema(type=openapi.TYPE_STRING),
                            "submittedBy": openapi.Schema(type=openapi.TYPE_STRING),
                            "submittedDate": openapi.Schema(type=openapi.TYPE_STRING),
                            "fields": openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    ),
            )
        }
    )
    def post(self, request):
        # import pdb; pdb.set_trace()
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                custom_response.create_response("Wheel specification submitted successfully.", serializer.data),
                status=status.HTTP_201_CREATED
            )
    
        return Response(
           custom_response.serializers_errors(serializer.errors),
        status=status.HTTP_400_BAD_REQUEST
        )
            
