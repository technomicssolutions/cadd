function attendance_validation($scope, $http){
    $scope.validation_error = "";
    if($scope.students.length == 0){
        $scope.validation_error = 'No students in this batch ';
        return false;
    } else if($scope.batch.id == '') {
        $scope.validation_error = 'Please choose batch';
        return false;
    } else if($scope.batch.topics == '') {
        $scope.validation_error = 'Please enter the topics covered';
        return false;
    } return true;
}
function student_search($scope, $http){
    $http.get('/admission/search_student/?name='+$scope.student_name+'&batch='+$scope.batch_id).success(function(data){
        if(data.result == 'ok')
            $scope.students_list = data.students;
        else
            $scope.message = data.message;
        }).error(function(data, status){
            console.log('Request failed'|| data);
        });
}
function AttendanceController($scope, $http, $element){
    $scope.batch_id = "";
    $scope.students = {}
    $scope.is_edit = false;   
    $scope.init = function(csrf_token) {
        $scope.csrf_token = csrf_token;
        get_batches($scope, $http);
        $scope.show_buttons = true;
        $scope.batch = {
            'id': '',
            'topics': '',
            'remarks': '',
        }
    }
    $scope.get_batch_details = function(batch){
        var url = '/attendance/batch_students/'+batch.id;
        $http.get(url).success(function(data)
        {
            console.log(data);
            $scope.students = data.students;
            $scope.current_month = data.current_month;
            $scope.current_year = data.current_year;
            $scope.current_date = data.current_date;
            $scope.batch.topics = data.topics;
            $scope.batch.remarks = data.remarks;
            $scope.batch.staff = data.staff;
            for(var i = 0; i < $scope.students.length; i++){
                if($scope.students[i].is_presented == 'true')
                    $scope.students[i].is_presented = true;
                else 
                    $scope.students[i].is_presented = false;
            }
            if($scope.students.length == 0)
                $scope.validation_error = "No students in this batch";
            else
                $scope.validation_error = "";
        }).error(function(data, status){

        });
    }
    $scope.appliedClass = function(day) {
        if (day.is_holiday == 'true'){
            return "red_color";
        } 
        else if(day.is_future_date == 'true') {
          return "blue_color";  
        }
    }

    $scope.edit_attendance = function() {
        $scope.is_edit = true;
    }   

    $scope.save_attendance = function() {
        if(attendance_validation($scope, $http)) {
           for(var i = 0; i < $scope.students.length; i++){
                if($scope.students[i].is_presented == true)
                    $scope.students[i].is_presented = 'true';
                else
                    $scope.students[i].is_presented = 'false';
           }
            params = { 
                'batch': angular.toJson($scope.batch),
                'students': angular.toJson($scope.students),
                'current_month': $scope.current_month,
                'current_year': $scope.current_year,
                'current_date': $scope.current_date,
                "csrfmiddlewaretoken" : $scope.csrf_token
            }
            show_spinner();
            $http({
                method : 'post',
                url : '/attendance/add_attendance/',
                data : $.param(params),
                headers : {
                    'Content-Type' : 'application/x-www-form-urlencoded'
                }
            }).success(function(data, status) {
                hide_spinner();
                document.location.href = '/attendance/add_attendance/';
                $('#overlay').css('height', '0px');
                $('#spinner').css('height', '0px');
            }).error(function(data, status){
                console.log('error - ', data);
                $('#overlay').css('height', '0px');
                $('#spinner').css('height', '0px');
            });
        }
    }
}

function AttendanceDetailsController($scope, $element, $http) {

    $scope.year = [];
    $scope.batch_month = '';
    $scope.batch_year = '';
    $scope.init = function(csrf_token) {
        $scope.csrf_token = csrf_token;
        get_batches($scope, $http);
        $scope.batch_id = '';
        $scope.monthly_attendance = false
        $scope.show_batch_select = false
        $scope.daily_attendance = false;
        $scope.show_buttons = false;
        $scope.show_data = false;
        $scope.batch = {
            'id': '',
            'staff': '',
            'remarks': '',
            'topics': '',
        }
        new Picker.Date($$('#attendance_date'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
    }
    var date = new Date();
    var current_year = date.getFullYear(); 
    var start_year = current_year - 4;
    current_year = current_year + 4;
    for(var i=start_year; i<=current_year; i++){
        $scope.year.push(i);
    }
    $scope.attendance_validation = function() {
        $scope.validation_error = "";
        if($scope.attendance_view == "1" || $scope.attendance_view == undefined){
            if($scope.batch_id == '' || $scope.batch_id == undefined) {
                $scope.validation_error = 'Please choose the Batch';
                return false;
            } else if($scope.batch_month == '' || $scope.batch_month == undefined) {
                $scope.validation_error = 'Please choose the Month';
                return false;
            } else if($scope.batch_year == '' || $scope.batch_year == undefined) {
                $scope.validation_error = 'Please choose the Year';
                return false;
            } return true;
        }
        else if($scope.attendance_view == "2"){
            $scope.attendance_date = $$('#attendance_date')[0].get('value');
            if($scope.attendance_date == '' || $scope.attendance_date == undefined) {
                $scope.validation_error = 'Please choose the Date';
                return false;
            } return true;
        }

    }
    $scope.appliedClass = function(day) {
        if(day.is_future_date == 'true') {
          return "blue_color";  
        }
    }
    $scope.edit_attendance = function() {
        $scope.is_edit = true;
    }
    $scope.attendance_view_by = function(){
        $scope.validation_error = "";
        if($scope.attendance_view == "1"){            
            $scope.show_batch_select = true;
            $scope.monthly_attendance = true;
            $scope.daily_attendance = false;
            $scope.show_buttons = false;
            $scope.show_data = false;
            $scope.batch_id = "";
        }
        else if($scope.attendance_view == "2"){            
            $scope.show_batch_select = true;       
            $scope.daily_attendance = true;
            $scope.show_buttons = true;
            $scope.monthly_attendance = false;  
            $scope.show_data = false;         
            $scope.batch_id = "";
        }
    }
    $scope.get_attendance_details = function() {
        if ($scope.attendance_validation()) {
            $scope.validation_error = "";
            var height = $(document).height();
            height = height + 'px';
            $('#overlay').css('height', height);
            $('#spinner').css('height', height);
            $scope.validation_error = '';
            $scope.show_data = true;  
            if($scope.attendance_view == "1" || $scope.attendance_view == undefined){
                var url = '/attendance/attendance_details/?batch_id='+$scope.batch_id+'&batch_year='+$scope.batch_year+'&batch_month='+$scope.batch_month;                
            }
            else{
                $scope.attendance_date = $$('#attendance_date')[0].get('value');
                $scope.date_array = $scope.attendance_date.split('/')
                var url = '/attendance/attendance_details/?batch_id='+$scope.batch_id+'&batch_year='+$scope.date_array[2]+'&batch_month='+$scope.date_array[1]+'&batch_day='+$scope.date_array[0];
            }
            
            
            $http.get(url).success(function(data)
            {
                console.log(data);
                $scope.view = data.view;
                if($scope.view == 'monthly'){
                    $scope.students = data.batch[0].students;
                    $scope.columns = data.batch[0].column_count;  
                } else if($scope.view == 'daily'){
                    $scope.students = data.students;
                    $scope.batch.topics = data.topics;
                    $scope.batch.remarks = data.remarks;
                    $scope.batch.staff = data.staff;
                    $scope.batch.id = data.batch_id;
                    if(data.is_future_date == "true")
                        $scope.show_buttons = false;
                    else
                        $scope.show_buttons = true;
                    for(var i = 0; i < $scope.students.length; i++){
                        if($scope.students[i].is_presented == 'true')
                            $scope.students[i].is_presented = true;
                        else 
                            $scope.students[i].is_presented = false;
                    }
                }

                if ($scope.students.length == 0){
                    $scope.show_buttons = false;
                    $scope.validation_error = 'No Students';
                }
                $('#overlay').css('height', '0px');
                $('#spinner').css('height', '0px');
            }).error(function(data, status)
            {
                $('#overlay').css('height', '0px');
                $('#spinner').css('height', '0px');
                console.log(data || "Request failed");
            });
        }
    }
    $scope.save_attendance = function() {
        if(attendance_validation($scope, $http)) {
            var height = $(document).height();
            height = height + 'px';
           
            $('#overlay').css('height', height);
            $('#spinner').css('height', height);
            console.log($scope.batch);
            console.log($scope.students);
            for (var i=0; i < $scope.students.length; i++){
                if($scope.students[i].is_presented == true)
                    $scope.students[i].is_presented = "true";
                else
                    $scope.students[i].is_presented = "false";
            }
            $scope.attendance_date = $$('#attendance_date')[0].get('value');
            $scope.date_array = $scope.attendance_date.split('/')
            params = { 
                'batch': angular.toJson($scope.batch),
                'students': angular.toJson($scope.students),             
                'current_date': $scope.date_array[0], 
                'current_month': $scope.date_array[1],  
                'current_year': $scope.date_array[2],   
                "csrfmiddlewaretoken" : $scope.csrf_token
            }
            $http({
                method : 'post',
                url : '/attendance/add_attendance/',
                data : $.param(params),
                headers : {
                    'Content-Type' : 'application/x-www-form-urlencoded'
                }
            }).success(function(data, status) {
                document.location.href = '/attendance/attendance_details/';
                $('#overlay').css('height', '0px');
                $('#spinner').css('height', '0px');
            }).error(function(data, status){
                console.log('error - ', data);
                $('#overlay').css('height', '0px');
                $('#spinner').css('height', '0px');
            });
        }
    }
    $scope.clear_batch_details = function() {
        $scope.attendance_view = 1;
        if ($scope.attendance_validation()) {
            $scope.popup = new DialogueModelWindow({
                
                'dialogue_popup_width': '20%',
                'message_padding': '0px',
                'left': '28%',
                'top': '182px',
                'height': 'auto',
                'content_div': '#clear_batch_details_message'
            });
            var height = $(document).height();
            $scope.popup.set_overlay_height(height);
            $scope.popup.show_content();
        }
    }
    $scope.clear_batch = function(){
        $scope.batch_id = '';
        $scope.show_data = false;
        $scope.show_buttons = false;
        $scope.is_edit = false;
    }
    $scope.clear_ok = function() {
        document.location.href = '/attendance/clear_batch_details/?batch_id='+$scope.batch_id+'&batch_year='+$scope.batch_year+'&batch_month='+$scope.batch_month;
    }
    $scope.clear_cancel = function() {
        $scope.popup.hide_popup();
    }
}

function JobCardController($scope, $http){
    $scope.init = function(){
        get_batches($scope, $http);
        $scope.batch_id = "";
        $scope.student_name = "";
        $scope.job_card = {
            'batch_id': '',
            'student_id': '',
        };
    }
    $scope.student_search = function(){
        if($scope.student_name.length > 0){
            $scope.message = "";
            if($scope.batch_id != '')
                student_search($scope, $http);
            else
                $scope.message = "Please select a Batch";
        }
    }
    $scope.select_batch = function(){
        $scope.student_name = "";
        $scope.message = "";
        $scope.job_card = {
            'batch_id': '',
            'student_id': '',
        };
    }
}