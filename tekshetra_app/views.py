from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProfessionalSerializer

@api_view(["POST"])
def submit_professional(request):
    serializer = ProfessionalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    return Response({"status": "error", "errors": serializer.errors}, status=400)
