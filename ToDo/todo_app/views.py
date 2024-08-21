from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import todomodel
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = todomodel.objects.all()
    serializer_class = TodoSerializer

    #GET
    def list(self, request):
        todos = self.get_queryset()
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)

    #POST
    def create(self, request):
        serializer = self.get_serializer(data=request.data)# this validates the data
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer) #save the data to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    #GET
    def retrieve(self, request, pk=None):
        todo = self.get_object()# fetch a specific queryset
        serializer = self.get_serializer(todo)#initializes the TodoSerializer with todo object and preparing it to convert the todo instance into JSON format.
        return Response(serializer.data)

    #PUT
    def update(self, request, pk=None):
        todo = self.get_object()
        serializer = self.get_serializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    #PATCH
    def partial_update(self, request, pk=None):
        todo = self.get_object()
        serializer = self.get_serializer(todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    #DELETE
    def destroy(self, request, pk=None):
        todo = self.get_object()
        self.perform_destroy(todo)
        return Response(status=status.HTTP_204_NO_CONTENT)
