"use strict";

var app = angular.module("myApp", ['ngResource',"ui.bootstrap",'uiSlider'], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

app.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "static/js/app/views/car_index.html",
                                
        })
        .when("/make_details/:make_name", {
            templateUrl: "static/js/app/views/car_index.html",
            controller: "MakeDetailCtrl",
            resolve: {
                models: function ($route, MakeDetailService) {
                    var make = $route.current.params.make_name
                    return MakeDetailService.get(make);
                    }
                  }     
        })
        .when("/:car_make/:car_model", {
            templateUrl: "static/js/app/views/car_index.html",
            controller: "ModelDetailCtrl",
            resolve: {
                modelset: function ($route, ModelDetailService) {
                    var car_make = $route.current.params.car_make
                    var model = $route.current.params.car_model
                    return ModelDetailService.get(car_make,model) ;
                    }
                  }     
        })
        .when("/:make_city/:car_make/:car_model",{
          templateUrl: "static/js/app/views/car_index.html",
          controller: "CityController",
          resolve: {
                makeset: function ($route, CityService) {
                    var city = $route.current.params.make_city
                    var make = $route.current.params.car_make
                    var model = $route.current.params.car_model
                    return CityService.get(city,make,model) ;
                    }
                  } 

        })
        .when("/:make_city",{
          templateUrl: "static/js/app/views/car_index.html",
          controller: "CityController",
          resolve: {
                makeset: function ($route, CityService) {
                    var city = $route.current.params.make_city
                    return CityService.city(city) ;
                    }
                  } 

        })
        .otherwise({
            redirectTo: '/'
        })
})
         

app.controller("myController", function($scope,$http,$location,MakeService,set_city)
    { 
        
        $scope.items = [];
            $scope.items.push({ title: 'Maruti Suzuki', models: ['Swift','Alto','Zen','800','A-Star'] });
            $scope.items.push({ title: 'Hyundai', models: ['Verna','Accent','Elantra','Santro','Sonata'] });
            $scope.items.push({ title: 'Honda', models: ['Accord','Amaze','Civic','City','CR-V'] });
            $scope.items.push({ title: 'Volkswagen', models: ['Vento','Beetle','Passat','Polo','Jetta']});
            $scope.items.push({ title: 'Tata', models: ['Safari','Indigo','Nano','Manza','Indica'] });
            $scope.items.push({ title: 'Toyota', models: ['Innova','Fortuner','Corolla','Altis','Camry'] });
            $scope.items.push({ title: 'Ford', models: ['Fusion','EcoSport','Endeavour','Ikon','Fiesta'] });
            $scope.items.push({ title: 'Chevrolet', models: ['Aveo','Aveo-Old','Aveo-U-VA','Captiva','Enjoy']});
            $scope.items.push({ title: 'Mahindra', models: ['Scorpio','Bolero','Xylo','Jeep','Quanto'] });
            $scope.items.push({ title: 'Skoda', models: ['Fabia','Laura','Superb','Octavia','Rapid'] });
         console.log($scope.items) 
         $scope.cities = ['Kolkata','Chandigarh','Bangalore','Mumbai','Delhi','Pune','Ahmedabad','Chennai','Noida','Hyderabad']; 
         // $scope.vote = false;
         // var check_id = 0;
         $scope.vote = true;
         $scope.show = function(vote,id){         
                  // if (check_id == id)
                  // {
                  //   $scope.vote = true;
                  //   console.log(id)
                  //   console.log($scope.vote)
                  // }
                  // else{
                  //   $scope.vote = false;
                  //   console.log(id)
                  //   console.log($scope.vote)
                  // }
                    
               };

        $scope.onChange = function(item){
            $location.path(item);
            set_city.set_val(item) 
            };

        $scope.lower_price_bound = 0;
  $scope.upper_price_bound = 50;
  
  $scope.priceRange = function(item) {
    return (parseInt(item['min-acceptable-price']) >= $scope.lower_price_bound && parseInt(item['max-acceptable-price']) <= $scope.upper_price_bound);
  };          
});

app.factory('MakeService',['$resource',
    function($resource){
        return $resource('api/',{},{
            query:{method:'GET', params:{},isArray:true}
        });
    }
]);


app.service('set_city', function() {
    var city_name
 
    return {
        get_val: function() {
            return  city_name;
        },
        set_val: function(value) {
             city_name = value;
        }
    };
})



app.controller("CityController",function($scope,$http,$routeParams,CityService,makeset,set_city)
{ 


  $scope.models=makeset
  console.log($scope.models)
  $scope.CityFilter = set_city.get_val();
 
});


app.factory('CityService', function ($http, $q) {
    var api_url = "api/";
    return {
        get: function (city,make,model) {
            var url = api_url +city+ "/" + make + "/" + model +"/";
            var defer = $q.defer();
            $http({method: 'GET', url: url}).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                })
                .error(function (data, status, headers, config) {
                    defer.reject(status);
                });
            return defer.promise;
        },
        city: function(city){
            var url = api_url +city+ "/";
            var defer = $q.defer();
            $http({method: 'GET', url: url}).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                })
                .error(function (data, status, headers, config) {
                    defer.reject(status);
                });
            return defer.promise;
        }
        }
});





app.controller("MakeDetailCtrl", function($scope,$routeParams,MakeDetailService,models){
     

      $scope.master_make  = $routeParams.make_name
      
      console.log($scope.master_make)
      console.log("hai santhi")
      $scope.models = models
      console.log($scope.models)
     
      
        
 });    
 
app.factory('MakeDetailService', function ($http, $q) {
    var api_url = "api/";
    return {
        get: function (make) {
            var url = api_url +make+ "/";
            var defer = $q.defer();
            $http({method: 'GET', url: url}).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                })
                .error(function (data, status, headers, config) {
                    defer.reject(status);
                });
            return defer.promise;
        }
      }
});



 app.controller("ModelDetailCtrl", function($scope,$routeParams,ModelDetailService,modelset){
     
        $scope.car_model  = $routeParams.car_model
        $scope.car_model  = $routeParams.car_make
      
        $scope.models = modelset
        console.log($scope.models)
     
      
      

 });    
 
 
 app.factory('ModelDetailService', function ($http, $q) {
    var api_url = "api/";
    return {
        get: function (make,car_model) {
            var url = api_url + make + "/"+car_model+"/";
            var defer = $q.defer();
            $http({method: 'GET', url: url}).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                })
                .error(function (data, status, headers, config) {
                    defer.reject(status);
                });
            return defer.promise;
        }
      }
});
