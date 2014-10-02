

function add_new_student($http, $scope){  

    $scope.hide_popup_windows();
    $('#add_student_details')[0].setStyle('display', 'block');        
    $scope.popup = new DialogueModelWindow({

        'dialogue_popup_width': '79%',
        'message_padding': '0px',
        'left': '28%',
        'top': '182px',
        'height': 'auto',
        'content_div': '#add_student_details'
    });
    var height = $(document).height();
    $scope.popup.set_overlay_height(height);
    $scope.popup.show_content();
}

function save_new_student($http, $scope) {
    if(validate_new_student($scope)) {
        $scope.popup.hide_popup();
        var height = $(document).height();
        height = height + 'px';
        
        $('#overlay').css('height', height);
        $('#spinner').css('height', height);

        $scope.dob = $$('#dob')[0].get('value');
        $scope.doj = $$('#doj')[0].get('value');
        params = { 
            'student_name':$scope.student_name,
            'roll_number': $scope.roll_number,
            'course': $scope.course,
            'batch': $scope.batch,
            'semester': $scope.semester,           
            'qualified_exam': $scope.qualified_exam,
            'technical_qualification': $scope.technical_qualification,
            'dob': $scope.dob,
            'address': $scope.address,
            'mobile_number': $scope.mobile_number,
            'land_number': $scope.land_number,
            'email':$scope.email,
            'blood_group': $scope.blood_group,
            'doj': $scope.doj,
            'certificates_submitted': $scope.certificates_submitted,
            'certificates_remarks': $scope.certificates_remarks,
            'certificates_file': $scope.certificates_file,
            'id_proofs_submitted': $scope.id_proof,
            'id_proofs_remarks': $scope.id_proof_remarks,
            'id_proofs_file': $scope.id_proof_file,
            'guardian_name': $scope.guardian_name,
            'guardian_address':$scope.guardian_address,
            'relationship': $scope.relationship,
            'guardian_mobile_number': $scope.guardian_mobile_number,
            'guardian_land_number': $scope.guardian_land_number,
            'guardian_email': $scope.guardian_email,            
            "csrfmiddlewaretoken" : $scope.csrf_token
        }
        var fd = new FormData();

        fd.append('photo_img', $scope.photo_img.src)
        
        for(var key in params){
            fd.append(key, params[key]);          
        }
        var url = "/admission/add_student/";
        $http.post(url, fd, {
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined
            }
        }).success(function(data, status){
            if (data.result == 'error'){
                $scope.error_flag=true;
                $scope.validation_error = data.message;
                $scope.popup.set_overlay_height(height);
                $scope.popup.show_content();
                $('#spinner').css('height', '0px');
            }
            else {
                
                document.location.href ="/admission/list_student/";
            }

        }).error(function(data, status){
            $scope.error_flag=true;
            $scope.validation_error = data.message;
            $scope.popup.set_overlay_height(height);
            $scope.popup.show_content();
            $('#spinner').css('height', '0px');
        });
    }
}

function reset_student($scope) {
    $scope.student_name = '';
    $scope.roll_number = '';
    $scope.course = '';
    $scope.batch = '';
    $scope.semester = '';
    $scope.qualified_exam = '';
    $scope.technical_qualification = '';
    $scope.dob = '';
    $scope.address = '';
    $scope.mobile_number = '';
    $scope.land_number = '';
    $scope.email = '';
    $scope.blood_group = '';
    $scope.doj = '';
    $scope.certificates_submitted = '';
    $scope.certificates_remarks = '';
    $scope.certificates_file = '';
    $scope.id_proof = '';
    $scope.id_proof_remarks = '';
    $scope.id_proof_file = '';
    $scope.guardian_name = '';
    $scope.guardian_address = '';
    $scope.relationship = '';
    $scope.guardian_mobile_number = '';
    $scope.guardian_land_number = '';
    $scope.guardian_email    = '';
    $scope.photo_img = {};
}
validate_new_student = function($scope) {
    $scope.validation_error = '';
    $scope.dob = $$('#dob')[0].get('value');
    $scope.doj = $$('#doj')[0].get('value');

    if($scope.student_name == '' || $scope.student_name == undefined) {
        $scope.validation_error = "Please Enter the Name" ;
        return false;
    }   
    else if($scope.roll_number == '' || $scope.roll_number == undefined) {
        $scope.validation_error = "Please Enter the Roll Number" ;
        return false;
    }else if($scope.course == '' || $scope.course == undefined) {
        $scope.validation_error = "Please Enter Course";
        return false;
    }else if($scope.batch == '' || $scope.batch == undefined) {
        $scope.validation_error = "Please Enter Batch";
        return false;
    }else if($scope.dob == '' || $scope.dob == undefined) {
        $scope.validation_error = "Please Enter DOB";
        return false;
    } else if($scope.address == '' || $scope.address == undefined) {
        $scope.validation_error = "Please Enter Address";
        return false;
    } else if($scope.mobile_number == ''|| $scope.mobile_number == undefined){
        $scope.validation_error = "Please enter the Mobile Number";
        return false;
    } else if(!(Number($scope.mobile_number)) || $scope.mobile_number.length > 15) {            
        $scope.validation_error = "Please enter a Valid Mobile Number";
        return false;
    } else if($scope.land_number == ''|| $scope.land_number == undefined){
        $scope.validation_error = "Please enter the Telephone Number";
        return false;
    } else if(!(Number($scope.land_number)) || $scope.land_number.length > 15) {            
        $scope.validation_error = "Please enter a Valid Telephone Number";
        return false;
    } else if(($scope.email != '' && $scope.email != undefined) && (!(validateEmail($scope.email)))){
            $scope.validation_error = "Please enter a Valid Email Id";
            return false;
    } else if($scope.blood_group == '' || $scope.blood_group == undefined) {
        $scope.validation_error = "Please Enter Blood Group";
        return false; 
    } else if($scope.doj == '' || $scope.doj == undefined) {
        $scope.validation_error = "Please Enter Date of Join";
        return false;
    }else if($scope.certificates_submitted == '' || $scope.certificates_submitted == undefined) {
        $scope.validation_error = "Please enter certificates submitted";
        return false;
     } else if($scope.id_proof == '' || $scope.id_proof == undefined) {
         $scope.validation_error = "Please enter id proofs submitted";
        return false; 
    } else if($scope.guardian_name == '' || $scope.guardian_name == undefined) {
        $scope.validation_error = "Please Enter the Guardian Name" ;
        return false;
    
    } else if($scope.guardian_address == '' || $scope.guardian_address == undefined) {
        $scope.validation_error = "Please Enter Guardian Address";
        return false;
    } else if($scope.relationship == '' || $scope.relationship == undefined) {
        $scope.validation_error = "Please Enter Relationship";
        return false;
    } else if($scope.guardian_mobile_number == ''|| $scope.guardian_mobile_number == undefined){
        $scope.validation_error = "Please enter the Mobile Number";
        return false;
    } else if(!(Number($scope.guardian_mobile_number)) || $scope.guardian_mobile_number.length > 15) {            
        $scope.validation_error = "Please enter a Valid Mobile Number";
        return false;
    } else if($scope.guardian_land_number == ''|| $scope.guardian_land_number == undefined){
        $scope.validation_error = "Please enter the Telephone Number";
        return false;
    } else if(!(Number($scope.guardian_land_number)) || $scope.guardian_land_number.length > 15) {            
        $scope.validation_error = "Please enter a Valid Telephone Number";
        return false;
    } else if(($scope.guardian_email != '' && $scope.guardian_email != undefined) && (!(validateEmail($scope.guardian_email)))){
            $scope.validation_error = "Please enter a Valid Email Id";
            return false;                                                          
    } else {
        return true;
    }     
}   


function EditStudentController($scope, $http, $element, $location, $timeout) {
    $scope.init = function(csrf_token, student_id){

        $scope.csrf_token = csrf_token;
        $scope.student_id = student_id;
        
        $scope.url = '/admission/edit_student_details/' + $scope.student_id+ '/';
        $http.get($scope.url).success(function(data)
        {
            
            $scope.student = data.student[0];
            if ($scope.student.course_id)
                $scope.get_batch($scope.student.course_id);
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
        
        new Picker.Date($$('#dob'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
        new Picker.Date($$('#doj'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
        get_course_list($scope, $http);
        get_semester_list($scope, $http);
    }
    $scope.get_batch = function(course){        
        if (course)
            $scope.url_batch = '/college/get_batch/'+ course+ '/';
        else
            $scope.url_batch = '/college/get_batch/'+ $scope.course+ '/';
        $http.get($scope.url_batch).success(function(data)
        {
            $scope.batches = data.batches;
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
    $scope.validate_edit_student = function() {
        $scope.validation_error = '';
        $scope.dob = $$('#dob')[0].get('value');
        $scope.doj = $$('#doj')[0].get('value');

        if($scope.student.student_name == '' || $scope.student.student_name == undefined) {
            $scope.validation_error = "Please Enter the Name" ;
            return false;
        }   
        else if($scope.student.roll_number == '' || $scope.student.roll_number == undefined) {
            $scope.validation_error = "Please Enter the Roll Number" ;
            return false;
        }else if($scope.student.course == '' || $scope.student.course == undefined) {
            $scope.validation_error = "Please Enter Course";
            return false;
        }else if($scope.student.batch == '' || $scope.student.batch == undefined) {
            $scope.validation_error = "Please Enter Batch";
            return false;
        }else if($scope.student.dob == '' || $scope.student.dob == undefined) {
            $scope.validation_error = "Please Enter DOB";
            return false;
        } else if($scope.student.address == '' || $scope.student.address == undefined) {
            $scope.validation_error = "Please Enter Address";
            return false;
        } else if($scope.student.mobile_number == ''|| $scope.student.mobile_number == undefined){
            $scope.validation_error = "Please enter the Mobile Number";
            return false;
        } else if(!(Number($scope.student.mobile_number)) || $scope.student.mobile_number.length > 15) {            
            $scope.validation_error = "Please enter a Valid Mobile Number";
            return false;
        } else if($scope.student.land_number == ''|| $scope.student.land_number == undefined){
            $scope.validation_error = "Please enter the Telephone Number";
            return false;
        } else if(!(Number($scope.student.land_number)) || $scope.student.land_number.length > 15) {            
            $scope.validation_error = "Please enter a Valid Telephone Number";
            return false;
        } else if(($scope.student.email != '' && $scope.student.email != undefined) && (!(validateEmail($scope.student.email)))){
                $scope.validation_error = "Please enter a Valid Email Id";
                return false;
        } else if($scope.student.blood_group == '' || $scope.student.blood_group == undefined) {
            $scope.validation_error = "Please Enter Blood Group";
            return false; 
        } else if($scope.student.doj == '' || $scope.student.doj == undefined) {
            $scope.validation_error = "Please Enter Date of Join";
            return false;
        }else if($scope.student.certificates_submitted == '' || $scope.student.certificates_submitted == undefined) {
            $scope.validation_error = "Please enter certificates submitted";
            return false;
         } else if($scope.student.id_proofs_submitted == '' || $scope.student.id_proofs_submitted == undefined) {
             $scope.validation_error = "Please enter id proofs submitted";
            return false; 
        } else if($scope.student.guardian_name == '' || $scope.student.guardian_name == undefined) {
            $scope.validation_error = "Please Enter the Guardian Name" ;
            return false;
        
        } else if($scope.student.guardian_address == '' || $scope.student.guardian_address == undefined) {
            $scope.validation_error = "Please Enter Guardian Address";
            return false;
        } else if($scope.student.relationship == '' || $scope.student.relationship == undefined) {
            $scope.validation_error = "Please Enter Relationship";
            return false;
        } else if($scope.student.guardian_mobile_number == ''|| $scope.student.guardian_mobile_number == undefined){
            $scope.validation_error = "Please enter the Mobile Number";
            return false;
        } else if(!(Number($scope.student.guardian_mobile_number)) || $scope.student.guardian_mobile_number.length > 15) {            
            $scope.validation_error = "Please enter a Valid Mobile Number";
            return false;
        } else if($scope.student.guardian_land_number == ''|| $scope.student.guardian_land_number == undefined){
            $scope.validation_error = "Please enter the Telephone Number";
            return false;
        } else if(!(Number($scope.student.guardian_land_number)) || $scope.student.guardian_land_number.length > 15) {            
            $scope.validation_error = "Please enter a Valid Telephone Number";
            return false;
        } else if(($scope.student.guardian_email != '' && $scope.student.guardian_email != undefined) && (!(validateEmail($scope.student.guardian_email)))){
                $scope.validation_error = "Please enter a Valid Email Id";
                return false;
                                                              
        } else {
            return true;
        } 
        
    }   
    $scope.edit_student = function() {
        if ($scope.validate_edit_student()){
            $scope.error_flag=false;
            $scope.message = '';
           
            params = { 
                'student': angular.toJson($scope.student),
                "csrfmiddlewaretoken" : $scope.csrf_token
            }
            $http({
                method : 'post',
                url : $scope.url,
                data : $.param(params),
                headers : {
                    'Content-Type' : 'application/x-www-form-urlencoded'
                }
            }).success(function(data, status) {
                
                if (data.result == 'error'){
                    $scope.error_flag=true;
                    $scope.message = data.message;
                } else {
                    $scope.error_flag=false;
                    $scope.message = '';
                    document.location.href = '/admission/list_student/';
                }
            }).error(function(data, status){
                $scope.error_flag=true;
                $scope.message = data.message;
            });
        }
    }
}


function StudentListController($scope, $http, $element, $location, $timeout) {

    $scope.init = function(csrf_token){
        get_course_list($scope, $http);
        $scope.page_interval = 10;
        $scope.visible_list = [];
        $scope.students = [];
        $scope.csrf_token = csrf_token;
        $scope.error_flag = false;
        $scope.popup = '';      
        $scope.pages = 1;
        var date_pick = new Picker.Date($$('#dob'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
        
        new Picker.Date($$('#doj'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
        reset_student($scope);
    }
    $scope.get_batch = function(){        
        var url = '/college/get_batch/'+ $scope.course+ '/';
        $http.get(url).success(function(data)
        {
            $scope.batches = data.batches;
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
    $scope.get_students = function(){
        var url = '/admission/list_student/?batch_id='+ $scope.batch;
        $http.get(url).success(function(data)
        {
            $scope.students = data.students;
            paginate(data.students, $scope);
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
    $scope.add_new_student  = function(){
        add_new_student($http, $scope);
    }
    $scope.save_new_student = function(){
        save_new_student($http, $scope);
    }
    $scope.hide_popup_windows = function(){
        $('#add_student_details')[0].setStyle('display', 'none');
    }    
    $scope.display_student_details = function(student) {
        $scope.student_id = student.id;
        $scope.url = '/admission/view_student_details/' + $scope.student_id+ '/';
        $http.get($scope.url).success(function(data)
        {
            $scope.student = data.student[0];
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });

        $scope.hide_popup_windows();
        $('#student_details_view')[0].setStyle('display', 'block');
        
        $scope.popup = new DialogueModelWindow({                
            'dialogue_popup_width': '78%',
            'message_padding': '0px',
            'left': '28%',
            'top': '182px',
            'height': 'auto',
            'content_div': '#student_details_view'
        });
        
        var height = $(document).height();
        $scope.popup.set_overlay_height(height);
        $scope.popup.show_content();
    }
    $scope.close_popup = function(){
        $scope.popup.hide_popup();
    }
    $scope.select_page = function(page){
        select_page(page, $scope.students, $scope);
    }
    $scope.range = function(n) {
        return new Array(n);
    }
}
function EnquiryController($scope, $http) {
    $scope.enquiry = {
        'student_name' : '',
        'address' :'',
        'mobile_number' : '',
        'email' : '',
        'details_about_clients_enquiry' : '',
        'educational_qualification' : '',
        'land_mark' : '',
        'course' : '',
        'remarks': '',
        'follow_up_date' : '',
        'remarks_for_follow_up_date' : '',
        'discount' : '',
    }
    new Picker.Date($$('#follow_up_date'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
    });
    $scope.init = function(csrf_token){
        $scope.csrf_token = csrf_token;
        get_course_list($scope, $http);
    }
    $scope.validate_enquiry = function() {
    $scope.validation_error = '';
    $scope.enquiry.follow_up_date = $$('#follow_up_date')[0].get('value');
    

    if($scope.enquiry.student_name == '' || $scope.enquiry.student_name == undefined) {
        $scope.validation_error = "Please Enter the Name" ;
        return false;
    }else if($scope.enquiry.course == '' || $scope.enquiry.course == undefined) {
        $scope.validation_error = "Please Enter Course";
        return false;
    } 
    else if($scope.enquiry.address == '' || $scope.enquiry.address == undefined) {
        $scope.validation_error = "Please Enter Address";
        return false;
    } else if($scope.enquiry.mobile_number == ''|| $scope.enquiry.mobile_number == undefined){
        $scope.validation_error = "Please enter the Mobile Number";
        return false;
    } else if(!(Number($scope.enquiry.mobile_number)) || $scope.enquiry.mobile_number.length > 15) {            
        $scope.validation_error = "Please enter a Valid Mobile Number";
        return false;
    } else if(($scope.enquiry.email != '' && $scope.enquiry.email != undefined) && (!(validateEmail($scope.enquiry.email)))){
        $scope.validation_error = "Please enter a Valid Email Id";
        return false;
    } else if($scope.enquiry.follow_up_date == '' || $scope.enquiry.follow_up_date == undefined) {
        $scope.validation_error = "Please Enter follow up date";
        return false;
    }else {
        return true;
    }     
}   
    $scope.save_enquiry = function(){
         if ($scope.validate_enquiry()) {
            params = {
                'enquiry': angular.toJson($scope.enquiry),
                'csrfmiddlewaretoken': $scope.csrf_token,
                }
            
            $http({
                method: 'post',
                url: '/admission/enquiry/',
                data : $.param(params),
                headers : {
                    'Content-Type' : 'application/x-www-form-urlencoded'
                }
            }).success(function(data){
               
                if (data.result == 'ok') {
                    document.location.href = '/admission/enquiry/'    
                } 
            }).error(function(data, status){
                console.log('Request failed'||data);
            });
        }
    }
}
function AdmissionController($scope, $http) {
    $scope.show_enquiry_search =  false;
    $scope.show_admission_form = false;
    $scope.enquiry_num_exists = false;
    $scope.search = {
        'student_name': '',
        'enquiry_num': '',
    }
    $scope.init = function(csrf_token){
        $scope.csrf_token = csrf_token;
        $scope.no_enquiries = false;
        get_course_list($scope, $http);
    }
    $scope.enquiry_search  = function() {    
        var url = '/admission/enquiry_search/?student_name='+$scope.search.student_name;
        $http.get(url).success(function(data)
        {
            $scope.enquiries = data.enquiries; 
            $scope.count = data.count;
            if(data.enquiries.length <= 0){
              $scope.no_enquiries = true;

            } else {
              $scope.no_enquiries = false;
              $scope.show_admission_form = true;
              $scope.enquiry_num_exists = true;
            }
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
    $scope.change_admission_type = function(admission_type){
        if(admission_type=='Enquiry'){
            $scope.show_enquiry_search =  true;
            $scope.show_admission_form = false;
        }else{
            $scope.show_admission_form = true;
            $scope.show_enquiry_search =  false;
        }
    }
    $scope.get_enquiry_details = function(){
        var url = '/admission/enquiry_details/?enquiry_num='+$scope.enquiry_num;
        $http.get(url).success(function(data)
        {
            console.log(data)
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
    $scope.add_new_student  = function(){
        add_new_student($http, $scope);
    }
    $scope.save_new_student = function(){
        save_new_student($http, $scope);
    }
    $scope.hide_popup_windows = function(){
        $('#add_student_details')[0].setStyle('display', 'none');
    }  
    $scope.close_popup = function(){
        $scope.popup.hide_popup();
    } 
}
