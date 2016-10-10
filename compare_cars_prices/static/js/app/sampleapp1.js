"use strict";

var app = angular.module("myApp", ['uiSlider','ngRoute','ngResource',"ui.bootstrap"], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

app.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "static/js/app/views/car_index.html",
                                
        })
        .when("/:car_make/:car_model", {
            templateUrl: "static/js/app/views/car_index.html",
            controller: "MakeModelController",
            // resolve: {
            //    makeset: function ($route, CityService) {
            //         var car_make = $route.current.params.car_make
            //         var model = $route.current.params.car_model
            //         return CityService.model(car_make,model) ;
            //         }
            //       }     
        })
        .when("/:make_city/:car_make/:car_model",{
          templateUrl: "static/js/app/views/car_index.html",
          controller: "CityMakeModelController",
           

        })
        .when("/:make_city",{
          templateUrl: "static/js/app/views/car_index.html",
          controller: "CityController",

        })
        .otherwise({
            redirectTo: '/'
        })
})
         

// app.directive("loadMoreData", [function() {
//         console.log("hai")
//         return {
//             restrict: 'ACE',
//             link: function($scope, element, attrs, ctrl) {
//                 var raw = element[0];
//                 element.scroll(function() {
//                     console.log("hello")
//                     if (raw.scrollTop + raw.offsetHeight >= raw.scrollHeight){
//                         $scope.$apply("loadMoreData()");
//                     }
//                 });
//             }
//         };
 
// }])




app.controller("myController", function($scope,$http,$location,$timeout,MakeService,set_city)
    { 
        $scope.loading = true;    
        
        
       $scope.more = function(){
        MakeService.get().then(function(data) {
            $scope.models =  data;             
            $scope.loading = false;  
        });
       }
        
        $scope.more();

        $scope.items = [
                        { title: 'Maruti Suzuki', models: ['Swift','Alto','Zen','800','A-Star'] },
                        { title: 'Hyundai', models: ['Verna','Accent','Elantra','Santro','Sonata'] },
                        { title: 'Honda', models: ['Accord','Amaze','Civic','City','CR-V'] },
                        { title: 'Volkswagen', models: ['Vento','Beetle','Passat','Polo','Jetta']},
                        { title: 'Tata', models: ['Safari','Indigo','Nano','Manza','Indica'] },
                        { title: 'Toyota', models: ['Innova','Fortuner','Corolla','Altis','Camry'] },
                        { title: 'Ford', models: ['Fusion','EcoSport','Endeavour','Ikon','Fiesta'] },
                        { title: 'Chevrolet', models: ['Aveo','Aveo-Old','Aveo-U-VA','Captiva','Enjoy']},
                        { title: 'Mahindra', models: ['Scorpio','Bolero','Xylo','Jeep','Quanto'] },
                        { title: 'Skoda', models: ['Fabia','Laura','Superb','Octavia','Rapid'] }
                        ];
            
         console.log($scope.items) 
         $scope.cities = ['Kolkata','Chandigarh','Bangalore','Mumbai','Delhi','Pune','Ahmedabad','Chennai','Noida','Hyderabad']; 
        

        $scope.allData = false;
        $scope.firstOne = true;
        $scope.see_more = true;

        $scope.onAll = function () {
        $scope.firstOne = false;
        $scope.allData = true;
        $scope.see_more = false;          
        };

        $scope.show = function(){  
            $scope.allData = false;
            $scope.firstOne = true;  
            $scope.see_more = true;
        };
               

        $scope.onChange = function(item){
            $scope.allData = false;
            $scope.firstOne = true; 
            $scope.see_more = true;
            $location.path(item);
            set_city.set_val(item) 
            $scope.SearchFilter = "";
            };
       
    $scope.priceRange = function(item) {
    // console.log(item['price'])
    if ( item['price'] >= $scope.priceRange.low_price_bound && item['price'] <= $scope.priceRange.high_price_bound )
        return item;
    };

    $scope.priceRange.low_price_bound = 30000
    $scope.priceRange.high_price_bound = 9000000
  

           
});



app.factory('MakeService', function ($http, $q) {
    var api_url = "api/";
    return {
        get: function () {
            var url = api_url;
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
});



app.controller("CityController",function($scope,$http,$route,$routeParams,CityService,set_city)
{    
    var model = $route.current.params.car_model
    var city = $route.current.params.make_city
    var make = $route.current.params.car_make
    

    $scope.loading = true;  
    
    $scope.models = CityService.city(city).then(function(data) {
            $scope.models =  data; 
            console.log("CityController")
            $scope.loading = false;  
        });
    
    $scope.CityFilter = set_city.get_val();

    
 
});

app.controller("CityMakeModelController",function($scope,$http,$route,$routeParams,CityService,set_city)
{    
    var model = $route.current.params.car_model
    var city = $route.current.params.make_city
    var make = $route.current.params.car_make
    

    $scope.loading = true;  
    $scope.models = CityService.get(city,make,model).then(function(data) {
            $scope.models =  data; 
            console.log("CityMakeModelController")
            $scope.loading = false;  
        });
   
    $scope.CityFilter = set_city.get_val();
 
});


app.controller("MakeModelController",function($scope,$http,$route,$routeParams,CityService,set_city)
{    
    var model = $route.current.params.car_model
    var city = $route.current.params.make_city
    var make = $route.current.params.car_make
    

    $scope.loading = true;  
    $scope.models = CityService.model(make,model).then(function(data) {
            $scope.models =  data; 
            console.log("MakeModelController")
            $scope.loading = false;  
        });
   
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
        },
        model: function (make,model) {
            var url = api_url + make + "/"+model+"/";
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
})

app.directive("whenScrolled", function(){
  return{
    
    restrict: 'A',
    link: function(scope, elem, attrs){
    
      // we get a list of elements of size 1 and need the first element
      var raw = elem[0];
    
      // we load more elements when scrolled past a limit
      elem.bind("scroll", function(){
        if(raw.scrollTop+raw.offsetHeight+5 >= raw.scrollHeight){
          scope.loading = true;
          
        // we can give any function which loads more elements into the list
          scope.$apply(attrs.whenScrolled);
        }
      });
    }
  }
})




app.directive('ngEnter', function () {
    return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.ngEnter);
                });
 
                event.preventDefault();
            }
        });
    };
});

