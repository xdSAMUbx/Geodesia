
const mundo = document.getElementById("mundo");
const barraLateral = document.querySelector(".barra-lateral")
const span = document.querySelector("span")

mundo.addEventListener("click",()=>{
    barraLateral.classList.toggle("mini-barra-lateral");
    span.classList.toggle("oculto")
});