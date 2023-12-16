function ShowModal(){
    document.querySelector('.overlay').classList.add('showoverlay');
    document.querySelector('.loginform').classList.add('showloginform');
}
function CloseModal(){
    document.querySelector('.overlay').classList.remove('showoverlay');
    document.querySelector('.loginform').classList.remove('showloginform');
}
var btnlogin=document.querySelector('.btn-login');
btnlogin.addEventListener("click", ShowModal)

var c=document.querySelector('.close');
c.addEventListener("click", CloseModal)



function ShowModal1(){
    document.querySelector('.overlay1').classList.add('showoverlay1');
    document.querySelector('.bookform').classList.add('showbookform');
}
function CloseModal(){
    document.querySelector('.overlay1').classList.remove('showoverlay1');
    document.querySelector('.bookform').classList.remove('showbookform');
}
var btnlogin=document.querySelector('.btn-login1');
btnlogin.addEventListener("click", ShowModal)

var c=document.querySelector('.close1');
c.addEventListener("click", CloseModal)