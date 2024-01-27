document.getElementById("form").addEventListener("submit",x=>{
    x.preventDefault();
    redirect_home();
})

function redirect_home(){
    window.open("../html/home.html");
}