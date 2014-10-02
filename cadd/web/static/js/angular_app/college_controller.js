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

function CollegeController($scope, $element, $http, $timeout, share, $location)
{
    
    $scope.init = function(csrf_token)
    {
        $scope.popup = '';
        $scope.error_flag = false;
        $scope.software = {
            'id': '',
            'name': '',
        };
        $scope.csrf_token = csrf_token;
        get_software_list($scope, $http);
        //get_branch_list($scope, $http);
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
}
