from django.http import JsonResponse
from rest_framework.views import APIView

from ..serializers import SerializedCreateProperty

class PropertiesView(APIView):
    """
        View dedicated to:
            - Create a new properties
    """
    def post( self, request ):
        try:
            serialized_property = SerializedCreateProperty( data = request.data )
            serialized_property.is_valid()
            serialized_property.save()
            return JsonResponse(serialized_property.data, status=201)
        except Exception as e:
            return JsonResponse(serialized_property.errors, status=400)