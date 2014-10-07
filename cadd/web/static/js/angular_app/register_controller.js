function student_search_course($scope, $http){
    $http.get('/admission/search_student/?name='+$scope.student_name+'&course='+$scope.certificate.course).success(function(data){
        if(data.result == 'ok'){
            $scope.students_list = data.students;
            console.log($scope.students_list);
            if($scope.students_list.length == 0)
                $scope.validation_error = "No Students found";
        }            
        }).error(function(data, status){
            console.log('Request failed'|| data);
        });
}
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

function LetterController($scope, $element, $http, $timeout, share, $location) {
	$scope.init = function(csrf_token){
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

function CertificateController($scope, $element, $http, $timeout, share, $location) {
	$scope.certificate = {
		'id': '',
		'name': '',
		'date': '',
		'student': '',
		'course': '',
		'issued_authority': '',
	}
	$scope.init = function(csrf_token, certificate_id){
		$scope.csrf_token = csrf_token;
		get_course_list($scope, $http);
		new Picker.Date($$('#certificate_date'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
	}
	$scope.student_search = function(){
		if($scope.student_name.length > 0){
			$scope.validation_error = "";
			if($scope.certificate.course != ''){
				$scope.certificate.student = "";
                student_search_course($scope, $http);
            }                
            else
                $scope.validation_error = "Please select the Course";
		} 
		else 
			$scope.students_list = "";

	}
	$scope.select_course = function(){
		$scope.certificate.student = "";
		$scope.student_name = "";
		$scope.students_list = [];
	}
	$scope.get_student_details = function(student) {
        $scope.student_name = student.name;
        $scope.certificate.student = student.id;
        $scope.students_list = [];
        $scope.no_student_msg = "";
    }
	$scope.validate_certificate = function(){
		$scope.validation_error = "";
		$scope.certificate.date = $$('#certificate_date')[0].get('value');
		if($scope.certificate.name == ''){
			$scope.validation_error = "Please enter the certificate name";
			return false;
		} else if($scope.certificate.course == ''){
			$scope.validation_error = "Please select the course from the list";
			return false;
		} else if($scope.certificate.student == ''){
			$scope.validation_error = "Please select the student from the list";
			return false;
		} else if($scope.certificate.issued_authority == ''){
			$scope.validation_error = "Please enter the issued authority";
			return false;
		} else if($scope.certificate.date == ''){
			$scope.validation_error = "Please enter the date";
			return false;
		} return true;

	}
	$scope.cancel_certificate = function(){
		document.location.href ='/web/add_certificate/';
	}
	$scope.save_certificate = function(){
		if($scope.validate_certificate()){
            params = { 
                'certificate_details': angular.toJson($scope.certificate),
                "csrfmiddlewaretoken" : $scope.csrf_token
            }
            $http({
                method: 'post',
                url: "/web/add_certificate/",
                data: $.param(params),
                headers: {
                    'Content-Type' : 'application/x-www-form-urlencoded'
                }
            }).success(function(data, status) {
                if (data.result == 'error'){
                    $scope.validation_error = data.message;
                } else {
                    document.location.href ='/web/add_certificate/';
                }
            }).error(function(data, success){
                $scope.error_flag=true;
                $scope.validation_error = data.message;
            });
		}
	}

}