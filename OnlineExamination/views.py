from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from OnlineExamination.models import QuestionDb
from OnlineExamination.serializer import QuestionSerializer

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self, request):
        qs=QuestionDb.objects.all()
        serializer_instance=QuestionSerializer(qs,many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.create(**actual_data)
            return Response(data={"message":"Question added successfully."})
        else:
            return Response(data={"message":serializer_instance.errors})

class QuestionsRetrieveUpdateDeleteVeiw(APIView):
    def get(self, request, pk):
        qs=QuestionDb.objects.get(id=pk)
        serializer_instance=QuestionSerializer(qs)
        return Response(data={"message":serializer_instance.data})

    def put(self, request, pk):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.data
            QuestionDb.objects.filter(id=pk).update(**actual_data)
            return Response(data={'Message':'Data Updated'})
        else:
            return Response(data={'Message':serializer_instance.errors})

    def delete(self, request, pk):
        QuestionDb.objects.get(id=pk).delete()
        return Response(data={'Message':'Data Deleted'})