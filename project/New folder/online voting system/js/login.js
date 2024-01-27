document.getElementById("form").addEventListener("submit",x=>{
    x.preventDefault();
    redirect_rigestration();
})

function redirect_rigestration(){
    window.open("../html/home.html");
}