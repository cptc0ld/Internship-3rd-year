from market.api.serializers import ItemSerializer
from market import models
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Trade(APIView):
    def get(self, request, format=None):
        pass
        Items = models.Item.objects.all()
        serializer = ItemSerializer(Items, many=True)
        return Response(serializer.data)
