const nombre = document.getElementById("name");
const pass = document.getElementById("pass");
const codigo = document.getElementById("cod");
const form = document.getElementById("form");
const boton = document.getElementById("botonLogin");
const parrafo = document.getElementById("warnings");

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    parrafo.innerHTML = ""
    if(nombre.value.length <2){

       warnings += 'El nombre no es válido <br>' 
       entrar = true

    }

    if(pass.value.length <8){

        warnings += 'Carnet ID no válido <br>'
        entrar = true
 
     }

    if(codigo.value.length <5){

        warnings += 'El código no es válido <br>' 
        entrar = true
 
     }

     if(entrar){
         parrafo.innerHTML = warnings
     }else{

        if(pass.value == "admin123"){
            window.open("admin.html")
        }

        window.open("admin.html")

     }

})

