from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from FizzBuzz_App.models import FizzBuzz
from FizzBuzz_App.serializers import FizzBuzzSerializer


@api_view(["GET", 'POST'])
def fizzbuzz(request):
    """
    List all FizzBuzzes (GET), or create a new FizzBuzz (POST)
    """
    if request.method == 'GET':
        fizzbuzzes = FizzBuzz.objects.all()
        serializer = FizzBuzzSerializer(fizzbuzzes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data

        # if request includes a user agent, save it
        if 'HTTP_USER_AGENT' in request.META:
            data["useragent"] = request.META["HTTP_USER_AGENT"]

        serializer = FizzBuzzSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def fizzbuzz_detail(request, id):
    """
    Retrieve a single FizzBuzz object, given a fizzbuzz_id
    """
    try:
        instance = FizzBuzz.objects.get(pk=id)
    except:
        return Response({"Error message" : f"Requested FizzBuzz with id: {id} does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = FizzBuzzSerializer(instance)
    return Response(serializer.data)