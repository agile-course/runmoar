import json

from test_plus.test import TestCase

from .models import DateStatus
from .utils import getDateRange, toDate


class CompletionStatusViewTestCase(TestCase):

    """Abstracting superclass to hide test details and simplify for teaching"""

    def _execute_passing_test(self, start_date, end_date, expected):
        response = self.get_check_200('dateapi:completionStatus', data={
            'start_date': start_date,
            'end_date': end_date
        })
        self.assertIn('dates_completed', response.json())
        self.assertEquals(expected, response.json()['dates_completed'])

    def _execute_failing_test(self, start_date, end_date):
        data = {}
        if start_date:
            data['start_date'] = start_date
        if end_date:
            data['end_date'] = end_date
        response = self.get('dateapi:completionStatus', data=data)
        self.assertEqual(response.status_code, 400)


class ToggleStatusViewTestCase(TestCase):

    """Abstracting superclass to hide test details and simplify for teaching"""

    def _execute_passing_test(self, date):
        self.post(
            'dateapi:toggleStatus',
            data=json.dumps({'date': date}),
            extra={'content_type': 'application/json'}
        )
        self.response_200()


class GetDateAPIViewTests(CompletionStatusViewTestCase):

    def test_1weekrange(self):
        self._execute_passing_test(
            '2016-05-01',
            '2016-05-07',
            [False, False, False, False, False, False, False]
        )


class ToggleStatusAPIViewTests(ToggleStatusViewTestCase):

    def test_toggle_nonexsting_day(self):
        date = '2016-05-01'
        self._execute_passing_test(date)
        self.assertTrue(DateStatus.objects.get(date=date).completed)


class UtilTests(TestCase):

    def test_getDateRange(self):
        expected = [toDate('2016-05-01'), toDate('2016-05-02'), toDate('2016-05-03')]
        actual = getDateRange(toDate('2016-05-01'), toDate('2016-05-03'))
        self.assertEquals(expected, actual)
