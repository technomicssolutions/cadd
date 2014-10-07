function get_letters($scope, $http){
	$http.get("/web/letters/").success(function(data)
    {
        $scope.letters = data.letters;
        paginate($scope.letters, $scope);
    }).error(function(data, status)
    {
        console.log(data || "Request failed");
    });
}

function RegisterController($scope, $element, $http, $timeout, share, $location) {
	$scope.init = function(csrf_token, from){
		$scope.csrf_token = csrf_token;
		$scope.letter = {
			'type': '',
			'date': '',
			'from': '',
			'to': '',
		}
		get_letters($scope, $http);
	}
	$scope.create_popup = function(){
		new Picker.Date($$('#letter_date'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
		$scope.popup = new DialogueModelWindow({
            'dialogue_popup_width': '38%',
            'message_padding': '0px',
            'left': '28%',
            'top': '182px',
            'height': 'auto',
            'content_div': '#new_letter'
        });
        var height = $(document).height();
        $scope.popup.set_overlay_height(height);
        $scope.popup.show_content();
	}
	$scope.new_letter = function(){
		$scope.letter = {
			'id': '',
			'type': '',
			'date': '',
			'from': '',
			'to': '',
		}
		$scope.create_popup();
	}
	$scope.edit_letter = function(letter){
		$scope.letter = letter;
		$scope.create_popup();	
	}
	$scope.close_letter_popup = function(){
		$scope.popup.hide_popup();
	}
	$scope.validate_letter = function(){
		$scope.validation_error = "";
		$scope.letter.date = $$('#letter_date')[0].get('value');
		console.log($scope.letter.type);
		if($scope.letter.type == ''){
			$scope.validation_error = "Please Choose the letter type";
			return false;
		} else if($scope.letter.date == ''){
			$scope.validation_error = "Please enter the date";
			return false;
		} else if($scope.letter.from == ''){
			$scope.validation_error = "Please enter the From address";
			return false;
		} else if($scope.letter.to == ''){
			$scope.validation_error = "Please enter the To address";
			return false;
		} return true;
	}
	$scope.save_letter = function(){
		if($scope.validate_letter()) {
            params = { 
                'letter_details': angular.toJson($scope.letter),
                "csrfmiddlewaretoken" : $scope.csrf_token
            }
            $http({
                method: 'post',
                url: "/web/letters/",
                data: $.param(params),
                headers: {
                    'Content-Type' : 'application/x-www-form-urlencoded'
                }
            }).success(function(data, status) {
                if (data.result == 'error'){
                    $scope.validation_error = data.message;
                } else {
                    $scope.popup.hide_popup();
                    document.location.href ='/web/letters/';
                }
            }).error(function(data, success){
                $scope.error_flag=true;
                $scope.validation_error = data.message;
            });
        } 
	}
}
