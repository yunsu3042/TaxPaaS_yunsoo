from rest_framework import generics
from rest_framework import permissions
from autoinput.models import SourceDoc
from autoinput.serializers import SourceDocSerializer


class SourceDocCreateView(generics.CreateAPIView):
    queryset = SourceDoc.objects.all()
    serializer_class = SourceDocSerializer
    permissions = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        user = request.user
        user.tax
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}
