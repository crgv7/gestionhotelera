const nombre = document.getElementById("name");
const pass = document.getElementById("pass");
const cell = document.getElementById("cell");
const form = document.getElementById("form");
const parrafo = document.getElementById("warnings");

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    parrafo.innerHTML = ""
    if(nombre.value.length <2){

       warnings += 'El nombre no es válido <br>' 
       entrar = true

    }
    if(cell.value.length <8){

        warnings += 'El telefono no es válido <br>' 
        entrar = true
 
     }
    if(!regexEmail.test(email.value)){
       
        warnings += 'El email no es válido <br>'
        entrar = true

    }

    if(pass.value.length <6){

        warnings += 'La contraseña no es válida <br>'
        entrar = true
 
     }else if(pass2.value.length <6){

        warnings += 'La contraseña no es válida <br>'
        entrar = true
 
     }else if(pass.value != pass2.value){
        warnings += 'La contraseña no coincide<br>'
        entrar = true
     }

     if(entrar){
         parrafo.innerHTML = warnings
     }else{
        parrafo.innerHTML = "Registro exitoso"
     }

})
