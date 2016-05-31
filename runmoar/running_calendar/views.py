import json

from django.http import JsonResponse
from django.views.generic import View

from .models import DateStatus
from .utils import getDateRange, toDate


class GetDateAPIView(View):

    def get(self, request, *args, **kwargs):
        input_data = request.GET
        try:
            start_date = toDate(input_data['start_date'])
            end_date = toDate(input_data['end_date'])
        except KeyError:
            return JsonResponse(status=400, data={})

        dates_to_check = getDateRange(start_date, end_date)
        dates_completed = []
        for date in dates_to_check:
            try:
                dates_completed.append(DateStatus.objects.get(date=date).completed)
            except DateStatus.DoesNotExist:
                dates_completed.append(False)

        return JsonResponse(status=200, data={'dates_completed': dates_completed}, safe=False)


class ToggleStatusAPIView(View):

    def post(self, request, *args, **kwargs):
        input_data = json.loads(request.body)
        try:
            input_date = toDate(input_data['date'])
        except KeyError:
            return JsonResponse(status=400, data={})

        date_status, _ = DateStatus.objects.get_or_create(date=input_date)
        date_status.completed = not date_status.completed  # Toggle
        date_status.save()

        return JsonResponse(status=200, data={})
