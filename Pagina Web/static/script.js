
const mundo = document.getElementById("mundo");
const barraLateral = document.querySelector(".barra-lateral")
const spans = document.querySelectorAll("span")

mundo.addEventListener("click",()=>{
    barraLateral.classList.toggle("mini-barra-lateral");
    
    spans.forEach((span)=>{
        span.classList.toggle("oculto");
    });
});