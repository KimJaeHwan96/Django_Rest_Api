import ast
from copy import deepcopy
from datetime import datetime

from django.http import JsonResponse
from django.views.generic import View

from base.models import FakeModel


class FakeGenericView(View):
    """
    Django 의 View 중 가장 기본이 되는 View 를 이용한 View 클래스
    DetailView 와 ListView 는 response 가 템플릿으로 렌더링되도록 구현되어있어 View 만 사용했다.
    가장 기본이 되는 기능만 있어 각 HTTP Method 별로 메서드를 생성해줘야하고 Dispatch 는 HTTP Method 에 대해서만 검증한다.
    Permission, Error Handling, Authentication 등 중요한 기능이 빠져있어 View 만을 사용하려면 모든 것을 직접 구현해야한다.
    제대로된 View 클래스를 생성하기위해서는 DRF 를 이용할 필요가 있어보인다.
    해당 View 클래스는 가장 기초적인 기능만 간단히 구현했다.
    """
    model = FakeModel

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        if id:
            obj = self.model.objects.get(id=id)
            obj.__dict__.pop('_state')
            for key, value in obj.__dict__.items():
                if isinstance(value, datetime):
                    setattr(obj, f'{key}', value.strftime('%Y-%m-%d %H:%M:%S'))
            return JsonResponse(data=obj.__dict__)
        else:
            queryset = self.model.objects.all()
            queryset_list = []
            for query in queryset:
                query.__dict__.pop('_state')
                for key, value in query.__dict__.items():
                    if isinstance(value, datetime):
                        setattr(query, f'{key}', value.strftime('%Y-%m-%d %H:%M:%S'))
                queryset_list.append(query.__dict__)
            return JsonResponse(data=queryset_list, safe=False)

    def post(self, request, *args, **kwargs):
        post_body = request.POST
        obj = self.model.objects.create(**post_body)
        obj.__dict__.pop('_state')
        return JsonResponse(data=obj.__dict__, status=201)

    def put(self, request, *args, **kwargs):
        put_body = request.body.decode()
        put_body = ast.literal_eval(put_body)
        id = kwargs.get('pk', None)
        if not id:
            return JsonResponse(status=404, data={'error_msg': 'id 값을 입력하셔야 합니다.'})

        obj = self.model.objects.get(id=id)
        for field, value in put_body.items():
            setattr(obj, field, value)
        obj.save()
        obj.__dict__.pop('_state')
        return JsonResponse(data=obj.__dict__)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        if not id:
            return JsonResponse(status=404, data={'error_msg': 'id 값을 입력하셔야 합니다.'})

        obj = self.model.objects.get(id=id)
        deleted_obj = deepcopy(obj.__dict__)
        obj.delete()
        deleted_obj.pop('_state')
        return JsonResponse(data=deleted_obj, status=204)
