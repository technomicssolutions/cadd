'use strict';

/* Services */

// Demonstrate how to register services
// In this case it is a simple value service.
var cadd_serv = angular.module('cadd.services', ['ngResource']);

cadd_serv.value('version', '0.1');
cadd_serv.factory('share', function()
{
    return {
        messages : {
            show : false,
            type : '',
            message : ''
        },
        loader : {
            show : false
        }
    };
});
