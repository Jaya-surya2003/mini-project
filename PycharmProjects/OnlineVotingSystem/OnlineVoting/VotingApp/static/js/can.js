document.getElementById("form").addEventListener("submit",x=>{
    x.preventDefault();
    redirect_login();
})

function redirect_login(){
    window.open("../html/login.html");
}