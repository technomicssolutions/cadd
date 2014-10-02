
function get_software_list($scope, $http){
    $scope.url = '/college/softwares/';
    $http.get($scope.url).success(function(data)
    {        
        $scope.softwares = data.softwares; 
    }).error(function(data, status)
    {
        console.log(data || "Request failed");
    });
}
function get_batches($scope, $http){
    $scope.url = '/college/batches/';
    $http.get($scope.url).success(function(data)
    {        
        $scope.batches = data.batches;  
    }).error(function(data, status)
    {
        console.log(data || "Request failed");
    });
}
function get_course_list($scope, $http){
    $scope.url = '/college/courses/';
    $http.get($scope.url).success(function(data)
    {        
        $scope.courses = data.courses;  
        console.log($scope.courses) ;
    }).error(function(data, status)
    {
        console.log(data || "Request failed");
    });
}
function validate_batch($scope, $http){
    $scope.validation_error = '';
    if($scope.batch.name == ''){
        $scope.validation_error = "Please Enter name" ;
        return false;
    } else if($scope.batch.software == ''){
        $scope.validation_error = "Please Enter software" ;
        return false;
    } else if($scope.batch.start == '') {
        $scope.validation_error = "Please Enter Start time" ;
        return false;
    } else if($scope.batch.end == '') {
        $scope.validation_error = "Please Enter End time" ;
        return false;
    } else if($scope.batch.allowed_students == '') {
        $scope.validation_error = "Please Enter No of allowed students" ;
        return false;
    }  
    else {
        return true;
    } 
}
function save_batch($scope, $http){
    $scope.batch.start = $$('#batch_start')[0].get('value');
    $scope.batch.end = $$('#batch_end')[0].get('value');
    if(validate_batch($scope, $http)) {
        params = { 
            'batch': angular.toJson($scope.batch),
            "csrfmiddlewaretoken" : $scope.csrf_token
        }
        $http({
            method: 'post',
            url: "/college/add_new_batch/",
            data: $.param(params),
            headers: {
                'Content-Type' : 'application/x-www-form-urlencoded'
            }
        }).success(function(data, status) {
            
            if (data.result == 'error'){
                $scope.error_flag=true;
                $scope.message = data.message;
            } else {
                $scope.popup.hide_popup();
                $scope.batches.push(data.batch);

            }
        }).error(function(data, success){
            $scope.error_flag=true;
            $scope.message = data.message;
        });
    }
}
function CollegeController($scope, $element, $http, $timeout, share, $location)
{
    
    $scope.init = function(csrf_token, from)
    {
        console.log(from);
        $scope.popup = '';
        $scope.error_flag = false;
        $scope.csrf_token = csrf_token;
        if(from == 'softwares'){
            $scope.software = {
                'id': '',
                'name': '',
            };
            get_software_list($scope, $http);
        }
        if(from == 'courses'){
            $scope.course = {
                'id': '',
                'name': '',
                'duration': '',
                'duration_unit': '',
                'amount': '',
                'softwares': [],
            };
            $scope.softwares = [];
            get_course_list($scope, $http);
        }
    }
    $scope.edit_software = function(software){
        $scope.add_new_software();
        $scope.software.name = software.name;
        $scope.software.id = software.id;
    }
    $scope.delete_software = function(software){
        $scope.url = '/college/delete_software/'+software.id;
        $http.get($scope.url).success(function(data)
        {        
            $scope.message = data.message;
            document.location.href ='/college/softwares/';
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
    $scope.save_new_software = function() {
        if($scope.software.name != '') {
            params = { 
                'software_details': angular.toJson($scope.software),
                "csrfmiddlewaretoken" : $scope.csrf_token
            }
            $http({
                method: 'post',
                url: "/college/softwares/",
                data: $.param(params),
                headers: {
                    'Content-Type' : 'application/x-www-form-urlencoded'
                }
            }).success(function(data, status) {
                if (data.result == 'error'){
                    $scope.error_flag=true;
                    $scope.validation_error = data.message;
                } else {
                    $scope.popup.hide_popup();
                    document.location.href ='/college/softwares/';
                }
            }).error(function(data, success){
                $scope.error_flag=true;
                $scope.validation_error = data.message;
            });
        } else{
            $scope.validation_error = 'Software Name cannot be empty';
        }
    } 

    $scope.add_new_software = function(){  
        $scope.popup = new DialogueModelWindow({
            'dialogue_popup_width': '38%',
            'message_padding': '0px',
            'left': '28%',
            'top': '182px',
            'height': 'auto',
            'content_div': '#add_software'
        });
        var height = $(document).height();
        $scope.popup.set_overlay_height(height);
        $scope.popup.show_content();
    }
    $scope.close_software_popup = function(){
        $scope.software = {
            'id': '',
            'name': '',
        };
        $scope.validation_error = "";
        $scope.popup.hide_popup();
    }
    $scope.add_new_course = function(){  
        $scope.popup = new DialogueModelWindow({
            'dialogue_popup_width': '38%',
            'message_padding': '0px',
            'left': '28%',
            'top': '182px',
            'height': 'auto',
            'content_div': '#add_course'
        });
        var height = $(document).height();
        $scope.popup.set_overlay_height(height);
        $scope.popup.show_content();
        if($scope.course.id == '')
            get_software_list($scope, $http);
    }
    $scope.validate_course = function(){
        $scope.validation_error = "";
        console.log($scope.course.softwares);
        if($scope.course.name == ''){
            $scope.validation_error = 'Please enter course name';
            return false;
        } else if($scope.course.name == ''){
            $scope.validation_error = 'Please enter course name';
            return false;
        } else if($scope.course.softwares == ''){
            $scope.validation_error = 'Please choose atleast one software';
            return false;
        } else if($scope.course.duration == ''){
            $scope.validation_error = 'Please enter duration of the course';
            return false;
        } else if($scope.course.duration !== '' && !Number($scope.course.duration)){
            $scope.validation_error = 'Please enter a valid entry for duration';
            return false;
        } else if($scope.course.duration_unit == ''){
            $scope.validation_error = 'Please select the unit for duration';
            return false;
        } else if($scope.course.amount == ''){
            $scope.validation_error = 'Please enter amount of the course';
            return false;
        } else if($scope.course.amount !== '' && !Number($scope.course.amount)){
            $scope.validation_error = 'Please enter a valid amount';
            return false;
        } return true;
    }
    $scope.edit_course = function(course){
        $scope.course.id = course.id;
        $scope.course.name = course.name;
        $scope.course.duration = course.duration;
        $scope.course.amount = course.amount;
        $scope.course.duration_unit = course.duration_unit;
        $scope.url = '/college/softwares/';
        $http.get($scope.url).success(function(data)
        {        
            $scope.softwares = data.softwares;  
            for(var i = 0; i < $scope.softwares.length; i++){
                for(var j = 0; j < course.softwares.length; j++){
                    if($scope.softwares[i].id == course.softwares[j].id){
                        $scope.softwares[i].selected = 'true';
                        $scope.course.softwares.push($scope.softwares[i].id);
                    }
                }
            }
            console.log($scope.softwares);
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
        $scope.add_new_course();
    }
    $scope.delete_course = function(course){
        $scope.url = '/college/delete_course/'+course.id;
        $http.get($scope.url).success(function(data)
        {        
            $scope.message = data.message;
            document.location.href ='/college/courses/';
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
    $scope.save_new_course = function(){
        if($scope.validate_course()) {
            params = { 
                'course_details': angular.toJson($scope.course),
                "csrfmiddlewaretoken" : $scope.csrf_token
            }
            console.log($scope.course);
            $http({
                method: 'post',
                url: "/college/courses/",
                data: $.param(params),
                headers: {
                    'Content-Type' : 'application/x-www-form-urlencoded'
                }
            }).success(function(data, status) {
                if (data.result == 'error'){
                    $scope.error_flag=true;
                    $scope.validation_error = data.message;
                } else {
                    $scope.popup.hide_popup();
                    document.location.href ='/college/courses/';
                }
            }).error(function(data, success){
                $scope.error_flag=true;
                $scope.validation_error = data.message;
            });
        }
    }
    $scope.close_course_popup = function(){
        $scope.course = {
            'id': '',
            'name': '',
            'duration': '',
            'duration_unit': '',
            'amount': '',
            'softwares': [],
        };
        $scope.validation_error = "";
        $scope.popup.hide_popup();
    }
}



function EditBatchController($scope, $http, $element, $location, $timeout) {
    
    $scope.init = function(csrf_token, batch_id){
        $scope.csrf_token = csrf_token;
        $scope.url = '/college/edit_batch/' + batch_id + '/';
        $http.get($scope.url).success(function(data)
        {
            $scope.batch = data.batch[0];
            console.log($scope.batch);
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });

        new Picker.Date($$('#batch_start'), {
            timePicker: true,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            pickOnly: 'time',
            format:'%X',
            canAlwaysGoUp: ['time'],
            ampm: true,
        });
        new Picker.Date($$('#batch_end'), {
            timePicker: true,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            pickOnly: 'time',
            format:'%X',
            canAlwaysGoUp: ['time'],
            ampm: true,
        });
        get_software_list($scope, $http);
    }
    $scope.save_batch = function() {
        save_batch($scope, $http);
    }
}

function BatchController($scope, $element, $http, $timeout, share, $location)
{
    
    $scope.init = function(csrf_token)
    {
        $scope.popup = '';
        $scope.softwares = [];
        $scope.error_flag = false;
        $scope.csrf_token = csrf_token;
        $scope.batch = {
            'name': '',
            'software': '',
            'start': '',
            'end': '',
            'allowed_students': ''
        }
        get_software_list($scope, $http);
        get_batches($scope, $http);
        console.log($scope.softwares);
    }
    $scope.close_popup = function(){
        $scope.popup.hide_popup();
    }
    $scope.add_new_batch = function(){  
        new Picker.Date($$('#batch_start'), {
            timePicker: true,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            pickOnly: 'time',
            format:'%X',
            canAlwaysGoUp: ['time'],
            ampm: true,
        });
        
        new Picker.Date($$('#batch_end'), {
            timePicker: true,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            pickOnly: 'time',
            format:'%X',
            canAlwaysGoUp: ['time'],
            ampm: true,
        });
        $scope.popup = new DialogueModelWindow({
            'dialogue_popup_width': '38%',
            'message_padding': '0px',
            'left': '28%',
            'top': '182px',
            'height': 'auto',
            'content_div': '#add_batch'
        });
        var height = $(document).height();
        $scope.popup.set_overlay_height(height);
        $scope.popup.show_content();
        $scope.branch = '';
    }
    $scope.save_new_batch = function() {
        save_batch($scope, $http);
    } 

}
