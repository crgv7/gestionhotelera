const codigo = document.getElementById("cod");
const boton = document.getElementById("botonLogin");
const parrafo = document.getElementById("warnings");

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    parrafo.innerHTML = ""
    if(codigo.value.length == 0){

       warnings += 'Campo Vacío <br>' 
       entrar = true

    }

     if(entrar){
         parrafo.innerHTML = warnings
     }else{

        window.open("admin.html")

     }

})

