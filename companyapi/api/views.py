from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import Companyserializer, EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class = Companyserializer

### Like url will be http://localhost:8080/api/vi/{companyid}/employee
    @action(detail=True, methods=['get'])
    def Employee(self, request, pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializers=EmployeeSerializers(emps, many=True, context={'request':request})
            return Response(emps_serializers.data)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Company might not Exists !! Error'
            })
        
    


## Create Employee views
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class = EmployeeSerializers