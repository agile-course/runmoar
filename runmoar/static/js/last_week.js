app.controller('LastWeekController', function($scope, $resource, $filter) {
    var DateStatus = $resource(dateEndpointAPIURL + ":verb", {}, {
        'get': {
            method:'GET',
        },
        'toggle': {
            method:'POST',
            params: {
                verb: 'toggle'
            }
        },
    });
    // TODO | DRH | $filter(date) transform in $resource
    var dateFormat = 'yyyy-MM-dd';

    $scope.dates = [];
    for (i = 6; i >= 0; i--) {
        var d = new Date();
        d.setDate(d.getDate()-i);
        $scope.dates.push(d);
    }

    var getWeek = function() {
        $scope.dates_completed = [false, false, false, false, false, false, false];

        angular.forEach($scope.dates, function(date, index) {
            DateStatus.get({'date': $filter('date')(date, dateFormat)}, function(result) {
                $scope.dates_completed[index] = result.date_completed;
            });
        });
    };
    getWeek();

    $scope.toggleCompleted = function(date) {
        DateStatus.toggle({'date': $filter('date')(date, dateFormat)}, function(result) {
            getWeek();
        });
    };
});
