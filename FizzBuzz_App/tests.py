from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from FizzBuzz_App.models import FizzBuzz
from . import views

# Create your tests here.
class FizzBuzzTests(APITestCase):
    TEST_MESSAGE = "Hello, my name is fizzbuzz"

    def test_create_fizzbuzz_valid(self):
        """
        Test creating a new FizzBuzz with a valid request
        """
        factory = APIRequestFactory()
        request = factory.post('/fizzbuzz/', {'message' : self.TEST_MESSAGE})
        response = views.fizzbuzz(request)

        # check that we got the appropriate success status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        # check there is now 1 FizzBuzz objct in the test DB
        self.assertEqual(FizzBuzz.objects.count(), 1) 
        # check the object has the passed in message
        self.assertEqual(FizzBuzz.objects.first().message, self.TEST_MESSAGE)

    def test_create_fizzbuzz_invalid(self):
        """
        Test creating a new FizzBuzz with an invalid request
        """
        factory = APIRequestFactory()
        request = factory.post('/fizzbuzz/')
        response = views.fizzbuzz(request)

        # check that we got the appropriate bad request status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) 
        # check there are no FizzBuzz objects in the test DB
        self.assertEqual(FizzBuzz.objects.count(), 0) 

    def test_get_fizzbuzz(self):
        """
        Test retrieving a single FizzBuzz by ID
        """
        # First, manually create a few new FizzBuzz objs on the test DB
        FizzBuzz.objects.create(message = self.TEST_MESSAGE)
        FizzBuzz.objects.create(message = self.TEST_MESSAGE + "2")
        FizzBuzz.objects.create(message = self.TEST_MESSAGE + "3")

        factory = APIRequestFactory()
        request = factory.get('/fizzbuzz/1')
        response = views.fizzbuzz_detail(request, id=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # make sure its the object we expected
        self.assertEqual(response.data["message"], self.TEST_MESSAGE)
        self.assertEqual(response.data["fizzbuzz_id"], 1)


