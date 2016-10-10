"use strict";

var app = angular.module('myApp', ['ngRoute','ui.bootstrap','ng.django.urls'  ] );



app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');

});

app.config( function ( $routeProvider) {
    $routeProvider
    .when( '/', { templateUrl: 'views/makes.html' } )
    
    // .when('/movie/:Id', { templateUrl: 'movie.html', 
    //                       controller: "MovieCtrl"} )
     
     .when( '/compare_cars', { templateUrl: 'views/models.html' } )

    .otherwise( { redirectTo: '/home' } );
    
});





 app.controller("myController", ['$scope', '$http', 'djangoUrl', function($scope, $http, djangoUrl) 
   {    
                            
           console.log("")

    }]);
   

    
    


 // app.controller("modelController", function($scope,$routeParams){
     

 //      $scope.Id  = $routeParams.car_makes

    
 // });
 
// app.config( function ($stateProvider, $urlRouterProvider,) {
//     $urlRouterProvider.otherwise("/");
//     $stateProvider
//       .state('home', {
 
//              url: "/",
//              templateUrl: "/templates/home.html",
//              controller: "myController"
//          })
      
      
    
// });