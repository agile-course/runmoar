app.controller('CalendarController', function($scope) {
    $scope.dt = new Date();
    $scope.options = {
        customClass: getDayClass,
        minDate: new Date(),
        showWeeks: false
    };
    function getDayClass(data) {
        var date = data.date,
            mode = data.mode;
            if (mode === 'day') {
                var dayToCheck = new Date(date).setHours(0,0,0,0);
                // TODO Query for date completion
                return 'completed';
            }

            return '';
    }
});
