from rest_framework.response import Response
from rest_framework.decorators import api_view


# Response sert a retourner des réponses comme la librairie python Request.render pour afficher tout en JSON. 
# Le decorator c'est pour afficher la vue API

@api_view(['GET'])
def getData(request):
    person = {'name':'Damien', 'age': 28}
    return Response(person)