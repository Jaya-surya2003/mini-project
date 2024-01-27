document.getElementById("form").addEventListener("submit",x=>{
    x.preventDefault();
    redirect_can();
})

function redirect_can(){
    window.open("../html/can.html");
}