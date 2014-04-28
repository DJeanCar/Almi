
$('#ingresar').on('click',{id:2}, ocultandoMostrando);
$('#modal-content').on('mouseover',{id:0}, ocultandoMostrando);
$('#modal-content').on('mouseleave',{id:1}, ocultandoMostrando);

function ocultandoMostrando(event){
	if(event.data.id==0){
		console.log(event.data.id);
		$('#modal').click(function(){
			$(this).show();
			$('body').css({'overflow-y':'hidden'});
		});
	}

	if(event.data.id==1){
		console.log(event.data.id);
		$('#modal').click(function(){
			$(this).hide();
			$('body').css({'overflow-y':'visible'});
		});
	}

	if(event.data.id==2){
		console.log(event.data.id);
		$('#modal').show();
		$('body').css({'overflow-y':'hidden'});
		$('#modal').click(function(){
			$(this).hide();
			$('body').css({'overflow-y':'visible'});
		});
	}
}


//boton de configuración

$('.config-user').on('click', mostrandoConfiguracionUsuario);

function mostrandoConfiguracionUsuario(){
	$('.menu-user').toggle();
}

$('.menu-user').on('mouseleave',{id:1}, mostrando);

function mostrando(){
	if(valor.data.id==1){
		console.log('hola');
	}
}