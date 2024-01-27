
	var app = angular.module("header" ,["ngRoute"]);
app.controller("head",function($scope)
	{
		$scope.head = "BHARAT LOK SABHA ELECTION ";
		$scope.images = "../images/image8.jpg";

	});
app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "home.html"
    })
    .when("/cand", {
        templateUrl : "cand.html"
    })
    .when("/vote", {
        templateUrl : "vote.html"
    })
    .when("/curr", {
        templateUrl : "curr.php"
    });
});
document.getElementById("form").addEventListener("submit",x=>{
    x.preventDefault();
    redirect_can();
})

function redirect_can(){
    window.open("../html/can.html");
}