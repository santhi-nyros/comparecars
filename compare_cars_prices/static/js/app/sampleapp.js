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
        // .when("/:car_make/:car_model", {
        //     templateUrl: "static/js/app/views/car_index.html",
        //     controller: "MakeModelController",
            // resolve: {
            //    makeset: function ($route, CityService) {
            //         var car_make = $route.current.params.car_make
            //         var model = $route.current.params.car_model
            //         return CityService.model(car_make,model) ;
            //         }
            //       }     
        // })
        // .when("/search",{
        //   templateUrl: "static/js/app/views/car_index.html",
        //   controller: "searchController",
           

        // })
        .when("/seemore",{
          templateUrl: "static/js/app/views/car_index1.html",
          // controller: "CityController",

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





app.controller("myController", function($scope,$http,$location,$timeout,MakeService)
    { 
        $scope.loading = true;  
        $scope.display_limit = 3; 
        $scope.noMoreItemsAvailable = false;
        $scope.sample_data=[];
        $scope.models=[];
         $scope.indexlist=[];

       

       MakeService.get().then(function(data) {
            $scope.models =  data;
            $scope.loading=false;
                  
        });
        
        // var counter = 0;
        $scope.limit =3;
       $scope.more = function(){
        $scope.limit += 3;
        $scope.loading=false;

        // alert("loading")
     };

     $scope.send_result = function(result){
        $scope.result=result;
       } 
        $scope.onChange = function(text){
            // alert(text)
            MakeService.search(text).then(function(data){
                $scope.models = data;
                $scope.result =data;
                $scope.loading = false;            

            });
            // $scope.result();
        };

        $scope.go = function () {
            $location.path( "/" );
            for (var i=0;i<$scope.indexlist.length;i++)
            {
                var index = $scope.indexlist[i];
                $scope.items[index].checked = false;
            }
            $scope.DataIncludes=[];
            $scope.ModelIncludes=[];
            console.log($scope.indexlist)
        };
        
        $scope.items = [
                        { id:0,title: 'Maruti Suzuki', models: ['Swift','Alto','Zen','800','A-Star'],open: false,checked:false },
                        { id:1,title: 'Hyundai', models: ['Verna','Accent','Elantra','Santro','Sonata'],open: false,checked:false },
                        { id:2,title: 'Honda', models: ['Accord','Amaze','Civic','City','CR-V'],open: false,checked:false },
                        { id:3,title: 'Volkswagen', models: ['Vento','Beetle','Passat','Polo','Jetta'],open: false,checked:false},
                        { id:4,title: 'Tata', models: ['Safari','Indigo','Nano','Manza','Indica'],open: false,checked:false },
                        { id:5,title: 'Toyota', models: ['Innova','Fortuner','Corolla','Altis','Camry'],open: false,checked:false },
                        { id:6,title: 'Ford', models: ['Fusion','EcoSport','Endeavour','Ikon','Fiesta'],open: false,checked:false},
                        { id:7,title: 'Chevrolet', models: ['Aveo','Aveo-Old','Aveo-U-VA','Captiva','Enjoy'],open: false,checked:false},
                        { id:8,title: 'Mahindra', models: ['Scorpio','Bolero','Xylo','Jeep','Quanto'] ,open: false,checked:false},
                        { id:9,title: 'Skoda', models: ['Fabia','Laura','Superb','Octavia','Rapid'],open: false,checked:false }
                        ];
        $scope.cities = ['Kolkata','Chandigarh','Bangalore','Mumbai','Delhi','Pune','Ahmedabad','Chennai','Noida','Hyderabad']; 
        $scope.DataIncludes=[];
        $scope.ModelIncludes=[];


        //swamy

      /*  var counter = 0;

        $scope.loadMore = function() {
        for (var i = 0; i < 5; i++) {
            $scope.items.push({id: counter});
            counter += 10;
            }
        };
    
        $scope.loadMore();*/
        

        $scope.checkboxClick = function(make,index,model){
            $scope.indexlist.push(index);
            if(model){
                // console.log(model)
                // alert("not ok")
                $scope.items[index].checked = false;
                for (i=0;i<$scope.DataIncludes.length;i++){
                    var j = $scope.DataIncludes[i];
                    if (j == make)
                        $scope.DataIncludes.pop(make);

                }
                            
                console.log($scope.DataIncludes)
            }
            else{
                // alert("ok")
            $timeout(function () {
                $scope.items[index].checked = $scope.items[index].checked ? false : true;
                });
            var i = $.inArray(make, $scope.DataIncludes);
            if (i > -1) {
                $scope.DataIncludes.splice(i, 1);
                } else {
                    $scope.DataIncludes.push(make);
                    }                
                console.log($scope.DataIncludes)
            }
            };





        $scope.checkboxClick2 = function(index,model,make){
            // alert(item)
            $scope.checkboxClick(make,index,model);
            // alert(index)
            
            var i = $.inArray(model,$scope.ModelIncludes);
            if (i > -1) {
                $scope.ModelIncludes.splice(i, 1);
                } else {
                    $scope.ModelIncludes.push(model);
                    }
                console.log($scope.ModelIncludes)                           
            };

       $scope.modelFilter = function(item) {
            if ($scope.DataIncludes.length > 0) {
                if ($.inArray(item.car_make, $scope.DataIncludes) < 0){
                    // console.log("no car_make is not here,we going to model checking")
                    if ($scope.ModelIncludes.length >0){
                        // console.log("there is some models are selected,now check that models")
                        if($.inArray(item.car_model,$scope.ModelIncludes) < 0){
                            // console.log("no car_model is not here")
                            return;
                        }
                        console.log("not ok")
                        return item;
                        }
                    // return item;
                }
                // console.log("ok")
                for (var i=0;i<$scope.DataIncludes.length;i++){
                    var j = $scope.DataIncludes[i];
                    if (j == item.car_make)
                        return item;
                }
                // return item;
            }
            else{
                if ($scope.ModelIncludes.length > 0) {
                    if ($.inArray(item.car_model,$scope.ModelIncludes) < 0)
                        return;
                    }
                    return item;
                }
        
        };




        // $scope.checkboxClick2 = function(index,model){
        //     var i = $.inArray(model,$scope.ModelIncludes);
        //     if (i > -1) {
        //         $scope.ModelIncludes.splice(i, 1);
        //         } else {
        //             $scope.ModelIncludes.push(model);
        //             }
        //         console.log($scope.ModelIncludes)                           
        //     };        

        // $scope.modelFilter = function(item) {
        //     if ($scope.ModelIncludes.length > 0) {
        //         if ($.inArray(item.car_model,$scope.ModelIncludes) < 0)
        //             return;
        //         }
        //     return item;
        // };


  
        $scope.show = function(){  
            $scope.allData = false;
            $scope.firstOne = true;  
            $scope.see_more = true;
        };

        $scope.allData = false;
        $scope.firstOne = true;
        $scope.see_more = true;

        $scope.onAll = function () {
        $scope.firstOne = false;
        $scope.allData = true;
        $scope.see_more = false;          
        };
        // lazy loading
        var limitStep = 3;
        $scope.limit = limitStep;
        $scope.incrementLimit = function() {
        //alert("increment")
        $scope.limit += limitStep;
        };

        $scope.decrementLimit = function() {
        //alert("decrement")
        $scope.limit -= limitStep;
       };

       $scope.incrementLimit()

       //lazy loading end

        
       
    $scope.priceRange = function(item) {
    if ( item['price'] >= $scope.priceRange.low_price_bound && item['price'] <= $scope.priceRange.high_price_bound )
        return item;
    };





// Array.prototype.contains = function(element){
//     return this.indexOf(element) > -1;
// };
    $scope.priceRange.low_price_bound = 30000
    $scope.priceRange.high_price_bound = 9000000

function sticky_relocate() {
    var window_top = $(window).scrollTop();
    var div_top = $('#sticky-anchor').offset().top;
    if (window_top > div_top) {
        $('#sticky').addClass('stick');
    } else {
        $('#sticky').removeClass('stick');
    }
}

$(function () {
    $(window).scroll(sticky_relocate);
    sticky_relocate();
});
  


/*$scope.modelcheckboxClick = function(index){
    $timeout(function () {
      $scope.items[index].checked = $scope.items[index].checked ? false : true;
    });
  }*/



           
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
        },
        search:function(text){
            var url = api_url +text;
            var defer = $q.defer();
            $http({method: 'GET', url:url}).
                success(function(data, status, headers, config){
                    defer.resolve(data);
                })
                .error(function(data, status, headers, config){
                    defer.reject(status);
                });
            return defer.promise;
        }

    }
});

// app.service('set_city', function() {
//     var city_name
 
//     return {
//         get_val: function() {
//             return  city_name;
//         },
//         set_val: function(value) {
//              city_name = value;
//         }
//     };
// });



// app.controller("searchController",function($scope,$http,Ma)
// {    
//     // var model = $route.current.params.car_model
//     // var city = $route.current.params.make_city
//     // var make = $route.current.params.car_make
    

//     $scope.loading = true;  

//      $scope.onChange = function(text){
//             alert(text)
//             MakeService.search(text).then(function(data){
//                 $scope.models = data;
//                 $scope.loading = false;            
//             });
//         };
    
    
    
   
    
 
// });

// app.controller("CityMakeModelController",function($scope,$http,$route,$routeParams,CityService,set_city)
// {    
//     var model = $route.current.params.car_model
//     var city = $route.current.params.make_city
//     var make = $route.current.params.car_make
    

//     $scope.loading = true;  
//     $scope.models = CityService.get(city,make,model).then(function(data) {
//             $scope.models =  data; 
//             console.log("CityMakeModelController")
//             $scope.loading = false;  
//         });
   
//     $scope.CityFilter = set_city.get_val();
 
// });


// app.controller("MakeModelController",function($scope,$http,$route,$routeParams,CityService,set_city)
// {    
//     var model = $route.current.params.car_model
//     var city = $route.current.params.make_city
//     var make = $route.current.params.car_make
    

//     $scope.loading = true;  
//     $scope.models = CityService.model(make,model).then(function(data) {
//             $scope.models =  data; 
//             console.log("MakeModelController")
//             $scope.loading = false;  
//         });
   
//     $scope.CityFilter = set_city.get_val();
 
// });



// app.factory('CityService', function ($http, $q) {
//     var api_url = "api/";
//     return {
//         get: function (city,make,model) {
//             var url = api_url +city+ "/" + make + "/" + model +"/";
//             var defer = $q.defer();
//             $http({method: 'GET', url: url}).
//                 success(function (data, status, headers, config) {
//                     defer.resolve(data);
//                 })
//                 .error(function (data, status, headers, config) {
//                     defer.reject(status);
//                 });
//             return defer.promise;
//         },
//         city: function(city){
//             var url = api_url +city+ "/";
//             var defer = $q.defer();
//             $http({method: 'GET', url: url}).
//                 success(function (data, status, headers, config) {
//                     defer.resolve(data);
//                 })
//                 .error(function (data, status, headers, config) {
//                     defer.reject(status);
//                 });
//             return defer.promise;
//         },
//         model: function (make,model) {
//             var url = api_url + make + "/"+model+"/";
//             var defer = $q.defer();
//             $http({method: 'GET', url: url}).
//                 success(function (data, status, headers, config) {
//                     defer.resolve(data);
//                 })
//                 .error(function (data, status, headers, config) {
//                     defer.reject(status);
//                 });
//             return defer.promise;
//         }
//         }
// })

app.directive('scrollPosition', function ($window) {
  return function (scope, element, attrs) {      
    var w = element[0];
    //var w = $window;
    angular.element(w).bind('scroll', function () {                  
      scope.$apply(function () {                
        if (w.scrollTop + w.offsetHeight >= w.scrollHeight) {          
          scope.display_limit = scope.display_limit +3;
          
        }
      });
    });
  }
});


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

app.filter('unique', function() {
   return function(collection, keyname) {
      var output = [], 
          keys = [];

      angular.forEach(collection, function(item) {
          var key = item[keyname];
          if(keys.indexOf(key) === -1) {
              keys.push(key);
              output.push(item);
          }
      });

      return output;
   };
});

app.directive('whenScrolled', function($document, $window) {
    // alert("open")
    return function(scope, elm, attr) {
        var raw = elm[0];
        // alert("go to return")
        $document.bind('scroll', function() {
            
            if (raw.scrollTop + raw.offsetHeight >= raw.scrollHeight) {
                
                scope.$apply(attr.whenScrolled);
                console.log("fine")
            }
        });
    };
});


// app.directive('whenScrolled', function($document, $window) {
//     // alert("open")
//     return function(scope, elm, attr) {
//         // alert("ok")
//         var raw = elm[0];

//         $document.bind( 'scroll', function() {
//             // alert("fine")
//           if( ($window.innerHeight + $window.scrollY) > getDocHeight() - 100) {
//             alert("fine")
//                 scope.$apply(attr.whenScrolled);
//           } 
//         });
//     };
// });


/*function Main($scope) {
    $scope.items = [];
    
    var counter = 0;
    $scope.models=data;
    $scope.loadMore = function() {
        console.log('hai')
        MakeService.get().then(function(data1) {
            $scope.models =  data1; 
            console.log(data1)            
            $scope.loading = false;  
        });       

        for (var i = 0; i < 5; i++) {
            $scope.items.push({id: counter});
            counter += 10;
        }
        
    };
    
    $scope.loadMore();
}

app.directive('whenScrolled', function() {
    return function(scope, elm, attr) {
        var raw = elm[0];
        
        elm.bind('scroll', function() {
            if (raw.scrollTop + raw.offsetHeight >= raw.scrollHeight) {
                scope.$apply(attr.whenScrolled);
            }
        });
    };
});*/