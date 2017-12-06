from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from autoinput.models import W2
from autoinput.serializers import Ten99INTSerializer2, Ten99INTSerializer

__all__ = ('IntDetailView2', )


class IntDetailView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = W2.objects.all()
    serializer_class = Ten99INTSerializer2
    permission_classes = (permissions.IsAuthenticated,)

    # 나중에 url에 오는 단어를 기준으로 하나의 클래스에서 처리하게 할것
    # pk로 처리하게 되면 다른 사람의 개읹어보를 가져올 수 있기 때문에 큰일남
    # put에서 유저 정보 입력받음

    def update(self, request, *args, **kwargs):
        print(request.data)
        partial = True
        instance = self.get_object()
        data = request.data
        serializer = Ten99INTSerializer(instance, data=data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        print(serializer.data)

        last_serializer= Ten99INTSerializer2(instance)
        return Response(last_serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
