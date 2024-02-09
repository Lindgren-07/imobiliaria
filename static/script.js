var mensagem = document.querySelector('.menssagem_flash_excluir_all');

if (mensagem) {
    mensagem.classList.add('show'); 

    setTimeout(function() {
        mensagem.classList.remove('show'); 
    }, 4000);
}
