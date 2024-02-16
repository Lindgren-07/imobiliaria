
//CARROSEL
let cont = 1
document.getElementById("radio1").checked = true

setInterval( function(){
    nextImg()
}, 4000)

function nextImg(){
    cont++
    if(cont > 4){
        cont = 1
    }
    document.getElementById("radio"+cont).checked = true
}

//MODO CLARO E ESCURO
let chk = document.getElementById('chk')
let section = document.querySelector('.fundo_all')
let nav = document.querySelector('nav')
let footer = document.querySelector('footer')
let ancoras = document.querySelectorAll('.nav-link')

chk.addEventListener('change', () => {
    section.classList.toggle('dark')
    nav.classList.toggle('dark')
    footer.classList.toggle('dark')
    ancoras.forEach(anchor => {
        anchor.classList.toggle('dark')
    })
})
