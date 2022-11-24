from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view(['GET'])
def GetAddress(request, name):
    address = requests.get("https://api.iotexchartapp.com/bns/get-address/%s/" % (name)).json()["address"]
    data = {
        "address": address,
    }

    return Response(data)

@api_view(['GET'])
def GetName(request, address):
    name = requests.get("https://api.iotexchartapp.com/bns/get-name/%s/" % (address)).json()["name"]
    data = {
        "name": name,
    }

    return Response(data)

