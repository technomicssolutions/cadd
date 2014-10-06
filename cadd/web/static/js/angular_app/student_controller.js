

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

        $scope.dob = $$('#dob')[0].get('value');
        $scope.doj = $$('#doj')[0].get('value');
        for (var i=0; i<$scope.installments.length; i++) {
            id_name = '#'+$scope.installments[i].due_date_id;
            $scope.installments[i].due_date = $$(id_name)[0].get('value');
        }
        $scope.installments = angular.toJson($scope.installments)
        params = { 
            'enquiry': $scope.enquiry,
            'student_name':$scope.student_name,
            'roll_number': $scope.roll_number,
            'cadd_registration_no' : $scope.cadd_registration_no,
            'course': $scope.course,
            'batch': $scope.batch,        
            'qualifications': $scope.qualifications,
            'dob': $scope.dob,
            'address': $scope.address,
            'mobile_number': $scope.mobile_number,
            'email':$scope.email,
            'blood_group': $scope.blood_group,
            'doj': $scope.doj,
            'certificates_submitted': $scope.certificates_submitted,
            'id_proofs_submitted': $scope.id_proof,
            'guardian_name': $scope.guardian_name,
            'relationship': $scope.relationship,
            'guardian_mobile_number': $scope.guardian_mobile_number,
            'fees': $scope.fees,
            'installments': $scope.installments,
            'no_installments': $scope.no_installments,
            "csrfmiddlewaretoken" : $scope.csrf_token
        }
        console.log($scope.batch);
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
            }
            else {
                
                document.location.href ="/admission/student_admission/";
            }

        }).error(function(data, status){
            $scope.error_flag=true;
            $scope.validation_error = data.message;
            $('#spinner').css('height', '0px');
        });
    }
}

function reset_student($scope) {
    $scope.student_name = '';
    $scope.roll_number = '';
    $scope.cadd_registration_no = '';
    $scope.course = '';
    $scope.batch = '';
    $scope.semester = '';
    $scope.qualifications = '';
    $scope.dob = '';
    $scope.address = '';
    $scope.mobile_number = '';
    $scope.email = '';
    $scope.blood_group = '';
    $scope.doj = '';
    $scope.certificates_submitted = '';
    $scope.id_proof = '';
    $scope.guardian_name = '';
    $scope.relationship = '';
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
    }  else if(($scope.email != '' && $scope.email != undefined) && (!(validateEmail($scope.email)))){
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
    
    }  else if($scope.relationship == '' || $scope.relationship == undefined) {
        $scope.validation_error = "Please Enter Relationship";
        return false;
    } else if($scope.guardian_mobile_number == ''|| $scope.guardian_mobile_number == undefined){
        $scope.validation_error = "Please enter the Guardian Mobile Number";
        return false;
    } else if(!(Number($scope.guardian_mobile_number)) || $scope.guardian_mobile_number.length > 15) {            
        $scope.validation_error = "Please enter a Valid Mobile Number";
        return false;
    } 
    console.log($scope.installments.length);
    for(var i = 0; i < $scope.installments.length; i++){
        id_name = '#'+$scope.installments[i].due_date_id;
        $scope.installments[i].due_date = $$(id_name)[0].get('value');
        if($scope.installments[i].amount == ''){
            $scope.validation_error = "Please enter the amount for installment";
            return false;
        } else if($scope.installments[i].amount && !Number($scope.installments[i].amount)){
            $scope.validation_error = "Please enter a valid amount for installment";
            return false;
        } else if($scope.installments[i].due_date == ''){
            $scope.validation_error = "Please enter the due date for installment";
            return false;
        } else if($scope.installments[i].fine && !Number($scope.installments.fine)){
            $scope.validation_error = "Please enter a valid fine amount for installment";
            return false;
        } 

    }
    return true;
         
}   
function EditStudentController($scope, $http, $element, $location, $timeout) {
    $scope.init = function(csrf_token, student_id){

        $scope.csrf_token = csrf_token;
        $scope.student_id = student_id;
        $scope.get_student_details(student_id);
        $scope.url = '/admission/edit_student_details/' + $scope.student_id+ '/';
        $http.get($scope.url).success(function(data)
        {
            
            $scope.student = data.student[0];
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
       
    }
    $scope.get_student_details  = function(student_id){
        $scope.url = '/admission/edit_student_details/' + student_id+ '/';
        $http.get($scope.url).success(function(data)
        {
            $scope.student = data.student[0];
            
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
        }  else if(($scope.student.email != '' && $scope.student.email != undefined) && (!(validateEmail($scope.student.email)))){
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
        
        }  else if($scope.student.relationship == '' || $scope.student.relationship == undefined) {
            $scope.validation_error = "Please Enter Relationship";
            return false;
        } else if($scope.student.guardian_mobile_number == ''|| $scope.student.guardian_mobile_number == undefined){
            $scope.validation_error = "Please enter the Mobile Number";
            return false;
        } else if(!(Number($scope.student.guardian_mobile_number)) || $scope.student.guardian_mobile_number.length > 15) {            
            $scope.validation_error = "Please enter a Valid Mobile Number";
            return false;
        }  else {
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

    $scope.init = function(csrf_token,student_id){
        get_batch_list($scope, $http);
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
    $scope.delete_students = function(student){
        $scope.student_id = student.id;
        var url = '/admission/delete_student_details/?batch_id=/'+ $scope.student_id+ '/';
        $http.get(url).success(function(data)
        {
            $scope.students = data.students;
            paginate(data.students, $scope);
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
    
    $scope.edit_student_details = function(student){
        $scope.student_id = student.id;
        document.location.href = '/admission/edit_student_details/'+ $scope.student_id+ '/';
        
       
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
        'date': '',
    }
    $scope.init = function(csrf_token){
        $scope.csrf_token = csrf_token;
        get_course_list($scope, $http);
        new Picker.Date($$('#follow_up_date'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
        new Picker.Date($$('#date'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
    }
    $scope.validate_enquiry = function() {
        $scope.validation_error = '';
        $scope.enquiry.follow_up_date = $$('#follow_up_date')[0].get('value');
        $scope.enquiry.date = $$('#date')[0].get('value');
        if($scope.enquiry.student_name == '' || $scope.enquiry.student_name == undefined) {
            $scope.validation_error = "Please Enter the Name" ;
            return false;
        } else if($scope.enquiry.course == '' || $scope.enquiry.course == undefined) {
            $scope.validation_error = "Please Enter Course";
            return false;
        } else if($scope.enquiry.address == '' || $scope.enquiry.address == undefined) {
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
        }  else if($scope.enquiry.date == '' || $scope.enquiry.date == undefined) {
            $scope.validation_error = "Please Enter  date of enquiry";
            return false;
        }return true;
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
    $scope.admission_type = 'Admission';
    $scope.photo_img = {};
    $scope.installments = [];
    $scope.search = {
        'student_name': '',
        'enquiry_num': '',
    }
    $scope.init = function(csrf_token){
        $scope.csrf_token = csrf_token;
        $scope.no_enquiries = false;
        get_course_list($scope, $http);
        get_batch_list($scope,$http);
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
    }
    $scope.enquiry_search  = function() {    
        var url = '/admission/enquiry_search/?student_name='+$scope.search.student_name;
        $http.get(url).success(function(data)
        {
            $scope.enquiries = data.enquiries; 
            $scope.count = data.count;
            if(data.enquiries.length == 0){
                $scope.no_enquiries = true;
            } else {
                $scope.no_enquiries = false;
            }
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
    $scope.change_admission_type = function(admission_type){
        if(admission_type=='Enquiry'){
            $scope.show_enquiry_search =  true;
        }else{
            $scope.show_enquiry_search =  false;
        }
    }
    $scope.get_enquiry_details = function(){
        var url = '/admission/enquiry_details/?enquiry_num='+$scope.enquiry_num;
        $http.get(url).success(function(data)
        {   
            $scope.no_enquiry_msg = '';
            if (data.enquiry.length == 0)
                $scope.no_enquiry_msg = 'No such enquiry';
            else {
                console.log(data.enquiry);
                $scope.student_name = data.enquiry[0].student_name;
                $scope.course = data.enquiry[0].course;
                $scope.address = data.enquiry[0].address;
                $scope.qualifications = data.enquiry[0].educational_qualification;
                $scope.email = data.enquiry[0].email;
                $scope.mobile_number = data.enquiry[0].mobile_number;
                $scope.enquiry = data.enquiry[0].id;
                $scope.get_fees();
            }
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
/*    $scope.validate_student = function(){
        $scope.validation_error = "";
        $scope.dob = $$('#dob')[0].get('value');
        if($scope.student_name == '' || $scope.student_name == undefined){
            $scope.validation_error = "Please enter the name of Student";
            return false;
        } else if($scope.course == '' || $scope.course == undefined){
            $scope.validation_error = "Please select the course";
            return false;
        } else if($scope.batch == '' || $scope.batch == undefined){
            $scope.validation_error = "Please select the batch";
            return false;
        } else if($scope.dob == '' || $scope.dob == undefined){
            $scope.validation_error = "Please enter the date of birth";
            return false;
        } else if($scope.address == '' || $scope.address == undefined){
            $scope.validation_error = "Please enter the address";
            return false;
        } else if($scope.mobile_number == '' || $scope.mobile_number == undefined){
            $scope.validation_error = "Please enter the mobile number";
            return false;
        } else if($scope.mobile_number && (!Number($scope.mobile_number) || $scope.mobile_number.length != 10)){
            $scope.validation_error = "Please enter a valid mobile number";
            return false;
        } else if($scope.blood_group == '' || $scope.blood_group == undefined){
            $scope.validation_error = "Please select the blood group";
            return false;
        } else if($scope.guardian_name == '' || $scope.guardian_name == undefined){
            $scope.validation_error = "Please enter the guardian name";
            return false;
        } else if($scope.relationship == '' || $scope.relationship == undefined){
            $scope.validation_error = "Please enter the relationship with guardian";
            return false;
        } else if($scope.fees && !Number($scope.fees)){
            $scope.validation_error = "Please enter a valid amount";
            return false;
        } 
        for(var i = 0; i < $scope.installments.length; i++){
            id_name = '#'+$scope.installments[i].due_date_id;
            $scope.installments[i].due_date = $$(id_name)[0].get('value');
            if($scope.installments[i].amount == ''){
                $scope.validation_error = "Please enter the amount for installment";
                return false;
            } else if($scope.installments[i].amount && !Number($scope.installments[i].amount)){
                $scope.validation_error = "Please enter a valid amount for installment";
                return false;
            } else if($scope.installments[i].due_date == ''){
                $scope.validation_error = "Please enter the due date for installment";
                return false;
            } else if($scope.installments[i].fine && !Number($scope.installments.fine)){
                $scope.validation_error = "Please enter a valid fine amount for installment";
                return false;
            } 

        }
        return true;      
    }*/
    $scope.save_new_student = function(){
        save_new_student($http, $scope);
    }
    $scope.load_installments = function() {
        if ($scope.no_installments > $scope.installments.length) {
            diff = $scope.no_installments - $scope.installments.length;
            for (var i=0; i<diff; i++) {
                due_date_id = 'due_date_'+$scope.installments.length;
                $scope.installments.push({
                    'amount': '',
                    'fine': '',
                    'due_date': '',
                    'due_date_id': due_date_id,
                })
            }
        } else {
            diff = $scope.installments.length - $scope.no_installments;
            for (var i=diff; i>0; i--) {
                index = $scope.installments.indexOf($scope.installments[$scope.installments.length])
                $scope.installments.splice(index, 1);
            }
        }
    }
    $scope.attach_date_picker = function(installment) {
        id_name = '#' +installment.due_date_id;
        new Picker.Date($$(id_name), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
    }
    $scope.get_fees = function() {
        for(var i=0; i<$scope.courses.length; i++) {
            if ($scope.course == $scope.courses[i].id) {
                $scope.fees = $scope.courses[i].amount;
            }
        }
    }
}
function EnquiryReportController($scope, $http) {
    $scope.start_date = '';
    $scope.end_date = '';
    $scope.init = function(csrf_token){
        $scope.csrf_token = csrf_token;
        new Picker.Date($$('#start_date'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
        new Picker.Date($$('#end_date'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
    }
    $scope.validate = function(){
        $scope.start_date = $$('#start_date')[0].get('value');
        $scope.end_date = $$('#end_date')[0].get('value');
        if($scope.start_date == ''){
            $scope.validate_error_msg = 'Please select the start date';
            return false;
        } else if($scope.end_date == ''){
            $scope.validate_error_msg = 'Please select the end date';
            return false;
        } return true;
    }
    $scope.view_enquiry = function(){
        if($scope.validate()){
            $http.get('/admission/enquiry_report?start_date='+$scope.start_date+'&end_date='+$scope.end_date).success(function(data){
                if(data.result=='ok'){
                    
                    $scope.enquiries = data.enquiries;
                }else{
                    $scope.validate_error_msg = "No enquiries  found";
                }
            }).error(function(data, status){
                $scope.message = data.message;
            })
        }
    } 
    $scope.get_enquiry_report = function(){
        $scope.start_date= $$('#start_date')[0].get('value');
        $scope.end_date = $$('#end_date')[0].get('value');
        document.location.href = '/admission/enquiry_report?start_date='+$scope.start_date+'&end_date='+$scope.end_date+'&report_type=pdf';
    }  
}
