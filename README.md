# gestion_tareas

las plantillas html estan en templates dentro de users
el plantillas css van dentro style-css que esta dentro de users

lo que debes hacer para ocultarlo es buscar el id del checkbox luego verificas si con :checked y entonces le pones ~ para escrbir el otro id y entonces le cambias el display como tu sabes hacerlo:
el contenido seria
#id_del_checkbox:checked ~ #id_del_contenidocambiante{contenido css}

en el caso de la tabla lo que se debe hacer es cojer la clase luegolo mismo pero como referencia se pondra la fila
.class:checked ~ tr{contenidocss}
