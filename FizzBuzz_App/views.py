from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from FizzBuzz_App.models import FizzBuzz
from FizzBuzz_App.serializers import FizzBuzzSerializer


@api_view(["GET", 'POST'])
def fizzbuzz(request):
    """
    List all FizzBuzzes, or create a new FizzBuzz
    """
    if request.method == 'GET':
        fizzbuzzes = FizzBuzz.objects.all()
        serializer = FizzBuzzSerializer(fizzbuzzes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        data["useragent"] = request.META["HTTP_USER_AGENT"]
        serializer = FizzBuzzSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)