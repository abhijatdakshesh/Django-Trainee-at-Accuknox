from rest_framework import serializers
from api.models import Company, Employee

#Create Serializers
class Companyserializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields = "__all__"

class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
        fields = '__all__'
