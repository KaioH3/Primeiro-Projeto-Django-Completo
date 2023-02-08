$(document).ready(function() {

    var deleteBtn = $('.delete-btn'); // selecionando o botão de delete através de sua classe: ".delete-btn"
    var searchBtn = $('#search-btn'); // id do botão que tem icone de lupa, o botão de pesquisar
    var searchForm = $('#search-form'); //id do formulario aonde o user escreverá a pesquisa

    $(deleteBtn).on('click', function(e){
        //função de callback para a lógica do botão deletar
        e.preventDefault(); // bloqueia o default do <a>, ou seja, quando o user clicar no botão de deletar, ele não acessará o /delete e não deletará a task

        var delLink = $(this).attr('href'); // pega o atributo deste(this) botão(deleteBtn)
        
        var result = confirm('Quer deletar esta tarefa?'); //mostra um alert com a pergunta, e com duas opções: ok ou cancelar
        
        if(result){
            // se o result estiver preenchido(ou for "ok")
            window.location.href = delLink; // com esta linha, o usuário é mandado para o link de deletar a tarefa
        }
    });

    $(searchBtn).on('click', function(){
        searchForm.submit(); // habilita o submit(quando você clica no botão search ou aperta o enter, ele envia pelos parametros da url)
    });

});



//console.log('funcionou')
//alert('funcinou mesmo')

