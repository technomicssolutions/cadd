function FeesPaymentController($scope, $element, $http, $timeout, share, $location)
{
    $scope.payment_installment = {
        'installment_id': '',
        'course_id': '',
        'batch_id': '',
        'student_id': '',
        'head_id': '',
        'paid_date': '',
        'total_amount': '',
        'paid_amount': 0,
        'paid_installment_amount': '',
        'balance': '',
        'student_fee_amount': '',
        'paid_fine_amount': '0',
        'fee_waiver': '0',
    }
    $scope.course = '';
    $scope.payment_installment.student = '';
    $scope.head = '';
    $scope.init = function(csrf_token)
    {
        $scope.csrf_token = csrf_token;
        var paid_date = new Picker.Date($$('#paid_date'), {
            timePicker: false,
            positionOffset: {x: 5, y: 0},
            pickerClass: 'datepicker_bootstrap',
            useFadeInOut: !Browser.ie,
            format:'%d/%m/%Y',
        });
        get_course_list($scope, $http);
    }
    $scope.get_student_list = function(){
        get_course_batch_student_list($scope, $http);
    }
    $scope.get_fees_head = function(){
        $scope.url = '/fees/get_fee_structure_head/'+ $scope.course+ '/'+ $scope.batch+ '/'+$scope.payment_installment.student+'/';
        if ($scope.course !='select' && $scope.batch != 'select' && $scope.payment_installment.student != 'select')
            $http.get($scope.url).success(function(data)
            {
                $scope.heads = data.heads;
                $scope.installments = [];
                $scope.payment_installment.amount = '';
                $scope.payment_installment.due_date = '';
                $scope.payment_installment.fine = '';
                $('#balance').val(0);
                $('#total_fee_amount').val(0);
                if ($scope.heads.length == 0) {
                    $scope.no_head_error = 'No fees structure for this batch';
                } else {
                    $scope.no_head_error = '';
                }
            }).error(function(data, status)
            {
                console.log(data || "Request failed");
            });
    }
    $scope.get_installment = function() {
        $scope.payment_installment.student = $scope.student.id;
        $scope.payment_installment.student_fee_amount = $scope.student.fees;
        $http.get('/admission/get_installment_details/?student='+$scope.payment_installment.student).success(function(data){
            if (data.installments.length == 0)
                $scope.no_installment_error = 'Payment completed';
            else
                $scope.no_installment_error = '';
            $scope.installments = data.installments;
            console.log($scope.installments);
            $('#due_date').val('');
            $('#fine_amount').val(0);
            $('#fee_amount').val(0);
            $('#total_fee_amount').val(0);
        }).error(function(data, status){
            console.log('Request failed', data);
        })
    }
    $scope.calculate_total_amount = function() {
        calculate_total_fee_amount();
    }
    $scope.get_fees = function(installment) {
        $scope.payment_installment.paid_date = installment.paid_date;
        $scope.payment_installment.due_date = installment.due_date;
        $scope.payment_installment.amount = installment.amount;
        $scope.payment_installment.fine = installment.fine_amount;
        $scope.payment_installment.paid_installment_amount = installment.paid_installment_amount;
        $scope.payment_installment.balance = installment.balance;
        $scope.payment_installment.total_amount_paid = installment.total_amount_paid;
        // $scope.payment_installment.installment_balance = $scope.payment_installment.amount - $scope.payment_installment.paid_installment_amount;
        $('#due_date').val(installment.due_date);
        $('#fine_amount').val(installment.fine_amount);
        $('#fee_amount').val(installment.amount);
        $('#balance').val(installment.balance);
        $('#installment_balance').val($scope.payment_installment.amount - $scope.payment_installment.paid_installment_amount);
        $('#installment_balance_amount').val($scope.payment_installment.amount - $scope.payment_installment.paid_installment_amount);
        $scope.payment_installment.total_balance = installment.course_balance;
        $scope.payment_installment.total_balance_amount = installment.course_balance;
        calculate_total_fee_amount();
    }
    $scope.calculate_balance = function() {
        $('#installment_balance').val(parseFloat($('#total_fee_amount').val()) - (parseFloat($scope.payment_installment.paid_amount) + parseFloat($scope.payment_installment.paid_installment_amount) + parseFloat($scope.payment_installment.paid_fine_amount)));
        $('#installment_balance').val(parseFloat($('#installment_balance').val()) - parseFloat($scope.payment_installment.fee_waiver));
        $scope.payment_installment.total_balance = parseFloat($scope.payment_installment.total_balance_amount) - (parseFloat($scope.payment_installment.paid_amount));
        $scope.payment_installment.total_balance = parseFloat($scope.payment_installment.total_balance) - parseFloat($scope.payment_installment.fee_waiver)
    }
    $scope.validate_fees_payment = function() {
        $scope.validation_error = '';

        var fine_balance = parseFloat($('#total_fee_amount').val()) - parseFloat($scope.payment_installment.amount);
        if($scope.course == '' || $scope.course == undefined) {
            $scope.validation_error = "Please Select a course " ;
            return false
        } else if($scope.payment_installment.student == '' || $scope.payment_installment.student == undefined) {
            $scope.validation_error = "Please select a student" ;
            return false;
        } else if($scope.installments.length == 0) {
            $scope.validation_error = "Payment completed" ;
            return false;
        } else if($scope.installment == '' || $scope.installment == undefined) {
            $scope.validation_error = "Please choose an installment" ;
            return false;
        } else if ($scope.payment_installment.paid_amount == '' || $scope.payment_installment.paid_amount == undefined) {
            $scope.validation_error = "Please enter paid amount" ;
            return false;
        } else if($scope.payment_installment.fee_waiver == ''){
            $scope.validation_error = "Please enter a valid amount in fee waiver" ;
            return false;
        } else if ($scope.payment_installment.paid_amount != Number($scope.payment_installment.paid_amount)) {
            $scope.validation_error = "Please enter valid paid amount" ;
            return false;
        } else if (fine_balance < $scope.payment_installment.paid_fine_amount ) {
            $scope.validation_error = "Please check the Paying Fine amount";
            return false;
        } else if ($scope.payment_installment.installment_balance < 0 ) {
            $scope.validation_error = "Please check the Paying amount";
            return false;
        } else if($scope.payment_installment.paid_fine_amount == ''){
            $scope.validation_error = "Please enter a valid amount in fine amount" ;
            return false;
        } return true; 
        // else if ($scope.payment_installment.paid_amount != $scope.payment_installment.balance) {
        //     $scope.validation_error = "Please check the balance amount with paid amount" ;
        //     return false;
        // } 
    }
    $scope.save_fees_payment = function() {

        $scope.payment_installment.course_id = $scope.course;
        $scope.payment_installment.installment_id = $scope.installment;
        $scope.payment_installment.paid_date = $$('#paid_date')[0].get('value');
        // $scope.payment_installment.total_amount = $$('#total_fee_amount')[0].get('value');
        $scope.payment_installment.total_amount = $$('#fee_amount')[0].get('value');
        $scope.payment_installment.installment_balance = $$('#installment_balance')[0].get('value');
        if($scope.validate_fees_payment()) {
            params = { 
                'fees_payment': angular.toJson($scope.payment_installment),
                "csrfmiddlewaretoken" : $scope.csrf_token,
            }
            $http({
                method: 'post',
                url: "/fees/fees_payment/",
                data: $.param(params),
                headers: {
                    'Content-Type' : 'application/x-www-form-urlencoded'
                }
            }).success(function(data, status) {
                
                if (data.result == 'error'){
                    $scope.validation_error = data.message;
                } else {              
                    document.location.href ="/fees/fees_payment/";
                }
            }).error(function(data, success){
                $scope.error_flag=true;
                $scope.message = data.message;
            });
        }
    }
}
function FeesController($scope, $element, $http, $timeout, share, $location)
{
    $scope.student_id = '';
    $scope.course = '';
    $scope.batch = '';
    $scope.fees_type = '';
    $scope.filtering_option = '';
    $scope.url = '';
    $scope.init = function(csrf_token)
    {
        $scope.csrf_token = csrf_token;
        $scope.error_flag = false;
        $scope.popup = '';
        get_course_list($scope, $http);
    }
    $scope.get_batch = function(){
        $scope.filtering_option = '';
        get_course_batch_list($scope, $http);
    }
    $scope.get_student = function(){
        $scope.fees_details = [];
        $scope.filtering_option = '';
        get_course_batch_student_list($scope, $http);
    }
    $scope.hide_popup_windows = function(){
        $('#fees_structure_details_view')[0].setStyle('display', 'none');
    }
    $scope.select_page = function(page){
        select_page(page, $scope.fees_details.students, $scope, 2);
    }
    $scope.range = function(n) {
        return new Array(n);
    }
    $scope.outstanding_fees_details = function(){ 
        $scope.url = '';
        if (($scope.fees_type != '' || $scope.fees_type != undefined) && ($scope.filtering_option != '' || $scope.filtering_option != undefined)) {
            if ($scope.course != 'select' && $scope.batch != 'select') {
                // if ($scope.filtering_option == 'student_wise' && $scope.student_id != 'select') {
                //     $scope.url = '/fees/get_outstanding_fees_details/?course='+$scope.course+ '&batch='+ $scope.batch+ '&student_id='+$scope.student_id+'&filtering_option='+$scope.filtering_option+'&fees_type='+$scope.fees_type;
                // } else {
                //     $scope.url = '/fees/get_outstanding_fees_details/?course='+$scope.course+ '&batch='+ $scope.batch+ '&filtering_option='+$scope.filtering_option+'&fees_type='+$scope.fees_type;
                // }
                $scope.url = '/fees/get_outstanding_fees_details/?course='+$scope.course+'&student_id='+$scope.student_id;
            }
        }
        $http.get($scope.url).success(function(data)
        {
            if (data.result == 'ok') {
                if (data.fees_details.length > 0) {
                    $scope.fees_details = data.fees_details[0];
                    if($scope.fees_details.students)
                        paginate($scope.fees_details.students, $scope, 2);
                } else {
                    $scope.fees_details = [];
                    $scope.fees_details.roll_no = data.roll_no
                    $scope.fees_details.student_name = data.student_name
                }
            } else {
                $scope.no_student_error = data.message;
            }
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }    
    $scope.close_popup = function(){
        $scope.popup.hide_popup();
    }   
    $scope.print_outstanding_fees_list = function() {
        document.location.href = '/fees/print_outstanding_fees_details/?student='+$scope.student_id;
    }
}

function FeesPaymentReportController($scope, $http, $element) {
    $scope.report_type = '';
    $scope.show_course_wise_report = false;
    $scope.show_student_wise_report = false;
    $scope.focusIndex = 0;
    $scope.keys = [];
    $scope.keys.push({ code: 13, action: function() { $scope.select_list_item( $scope.focusIndex ); }});
    $scope.keys.push({ code: 38, action: function() { 
        if($scope.focusIndex > 0){
            $scope.focusIndex--; 
        }
    }});
    $scope.keys.push({ code: 40, action: function() { 
        if($scope.focusIndex < $scope.students_list.length-1){
            $scope.focusIndex++; 
        }
    }});
    $scope.$on('keydown', function( msg, code ) {
        $scope.keys.forEach(function(o) {
          if ( o.code !== code ) { return; }
          o.action();
          $scope.$apply();
        });
    });
    $scope.init = function(csrf_token){
        $scope.csrf_token = csrf_token;
        $scope.error_flag = false;
        get_course_list($scope, $http);
    }
    $scope.select_list_item = function(index){
        student = $scope.students_list[index];
        $scope.get_report('student_wise',student);
    }
    $scope.change_report_type = function(report_type){
        if (report_type == 'course_wise'){
            $scope.show_course_wise_report = true;
            $scope.show_student_wise_report = false;
        }else {
            $scope.show_student_wise_report = true;
            $scope.show_course_wise_report = false;
        }
    }
    $scope.student_search = function(){
        if($scope.student_name.length > 0){
            $scope.validation_error = "";
            student_search($scope, $http);
        }
        else
            $scope.students_list = ""
    }
    $scope.get_report = function(report_type,student){
       
        if (report_type == 'student_wise') {
            document.location.href = '/fees/fees_payment_report/?&student_id='+student.id+'&report_type='+report_type;
        }else if(report_type == 'course_wise'){
            document.location.href = '/fees/fees_payment_report/?course='+$scope.course+ '&report_type='+report_type;
        }
    }
}
function UnRollController($scope, $http, $element) {
    $scope.init = function(csrf_token){
        $scope.csrf_token = csrf_token;
        $scope.error_flag = false;
        $scope.unroll_student_flag = true;
        $scope.roll_student_flag = true;
        get_course_list($scope, $http);
    }
    $scope.get_outstanding_student = function(){
        $scope.url = '/fees/get_outstanding_fees_details/?course='+$scope.course;
        $http.get($scope.url).success(function(data)
        {
            if (data.result == 'ok') {
                if (data.fees_details.length > 0) {
                    $scope.fees_details = data.fees_details[0];
                    if ($scope.fees_details.student_details.length == 0) {
                        $scope.no_student_error = "No students"
                    }
                    for(i=0;i<$scope.fees_details.student_details.length;i++){
                        $scope.no_student_error = '';
                        if($scope.fees_details.student_details[i].is_rolled == 'false'){
                            $scope.fees_details.student_details[i].is_rolled = false;
                            $scope.fees_details.student_details[i].is_unrolled = true;
                            // $scope.unroll_student_flag = true;
                        }else if($scope.fees_details.student_details[i].is_rolled == 'true'){
                            $scope.fees_details.student_details[i].is_unrolled = false;
                            $scope.fees_details.student_details[i].is_rolled = true;
                            // $scope.roll_student_flag = true;
                        }
                    }
                    // if($scope.fees_details.students)
                    //     paginate($scope.fees_details.students, $scope, 2);
                } else {
                    $scope.fees_details = [];
                    $scope.no_student_error = "No students"
                }
            } else {
                $scope.no_student_error = data.message;
            }
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
    $scope.unroll = function(student){
        // $scope.roll_student_flag = false;
        $scope.student_id = student.student_id;
        student.is_rolled = true;
        student.is_unrolled = false;
        $scope.url = '/fees/unroll_students/?student_id='+$scope.student_id;
        $http.get($scope.url).success(function(data)
        {
            if (data.result == 'ok') {
                
            } else {
                $scope.no_student_error = data.message;
            }
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
    $scope.roll = function(student){
        student.is_unrolled = true;
        student.is_rolled = false;
        // $scope.unroll_student_flag = false;
        $scope.student_id = student.student_id;
        $scope.url = '/fees/roll_students/?student_id='+$scope.student_id;
        $http.get($scope.url).success(function(data)
        {
            if (data.result == 'ok') {
                
            } else {
                $scope.no_student_error = data.message;
            }
        }).error(function(data, status)
        {
            console.log(data || "Request failed");
        });
    }
}