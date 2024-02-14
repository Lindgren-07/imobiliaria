var mensagem = document.querySelector('.menssagem_flash_excluir_all')

if (mensagem) {
    mensagem.classList.add('show')

    setTimeout(function() {
        mensagem.classList.remove('show')
    }, 4000)
}

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
