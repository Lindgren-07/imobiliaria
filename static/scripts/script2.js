//MENSAGEM SUMINDO
var mensagem = document.querySelector('.menssagem_flash_excluir_all')

if (mensagem) {
    mensagem.classList.add('show')

    setTimeout(function() {
        mensagem.classList.remove('show')
    }, 4000)
}


let chk = document.getElementById('chk')
let nav = document.querySelector('nav')
let footer = document.querySelector('footer')
let ancoras = document.querySelectorAll('.nav-link')

chk.addEventListener('change', () => {
    nav.classList.toggle('dark')
    footer.classList.toggle('dark')
    ancoras.forEach(anchor => {
        anchor.classList.toggle('dark')
    })
})
