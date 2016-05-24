from django.http import JsonResponse
from django.views.generic import View

from .models import DateStatus
from .utils import toDate


class GetDateAPIView(View):

    def get(self, request, *args, **kwargs):
        input_data = request.GET
        try:
            input_date = toDate(input_data['date'])
        except KeyError:
            return JsonResponse(status=400, data={})

        try:
            date_completed = DateStatus.objects.get(date=input_date).completed
        except DateStatus.DoesNotExist:
            date_completed = False

        return JsonResponse(status=200, data={'date_completed': date_completed}, safe=False)
