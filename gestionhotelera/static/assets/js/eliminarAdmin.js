const nombre = document.getElementById("name");
const boton = document.getElementById("botonLogin");
const parrafo = document.getElementById("warnings");

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    parrafo.innerHTML = ""
    if(nombre.value.length == 0){

       warnings += 'Campo Vacío <br>' 
       entrar = true

    }

     if(entrar){
         parrafo.innerHTML = warnings
     }else{

        window.open("admin.html")

     }

})

