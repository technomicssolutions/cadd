function get_software_list($scope, $http){
    $scope.url = '/college/list_softwares/';
    $http.get($scope.url).success(function(data)
    {        
        $scope.softwares = data.softwares[0];      
    }).error(function(data, status)
    {
        console.log(data || "Request failed");
    });
}

function CollegeController($scope, $element, $http, $timeout, share, $location)
{
    
    $scope.init = function(csrf_token)
    {
        $scope.popup = '';
        $scope.error_flag = false;
        $scope.csrf_token = csrf_token;
        get_software_list($scope, $http);
        //get_branch_list($scope, $http);
    }

    /*$scope.save_new_branch = function() {
        if(validate_new_branch($scope)) {
            params = { 
                'name': $scope.branch_name,
                'address': $scope.address,
                "csrfmiddlewaretoken" : $scope.csrf_token
            }
            $http({
                method: 'post',
                url: "/college/add_new_branch/",
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
                    document.location.href ='/college/list_branch/';
                }
            }).error(function(data, success){
                $scope.error_flag=true;
                $scope.message = data.message;
            });
        }
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
        get_semester_list($scope, $http);
    }
    $scope.close_popup = function(){
        $scope.popup.hide_popup();
    }*/
}
