//Mensaje no cambiar
$("#btnAddProducto").on("click", function Mensaje() {
    let carrito = JSON.parse(localStorage.getItem("carrito"))
    let index = carrito.findIndex(object => {
        return object.id_producto === idProducto;
    })


    const msgDiv = $("#msgAgregar")

    if (msgDiv.attr('id') == "msgAgregar") {
        console.log("ya existe");
        msgDiv.remove()
    }

    const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
    const appendAlert = (message, type) => {
        const wrapper = document.createElement('div')
            wrapper.innerHTML = [
                `<div id="msgAgregar" class="alert alert-${type} alert-dismissible" role="alert">`,
                `   <div>${message}</div>`,
                '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
                '</div>'
            ].join('')
        
        

        alertPlaceholder.append(wrapper)
    }
    
        appendAlert('Producto agregado correctamente', 'success')
    
    

    
    setTimeout(eliminarMensaje, 5000)
})


function eliminarMensaje() {
    const msgEliminar = $("#msgAgregar")
    if (msgEliminar.attr('id') == "msgAgregar") {
        msgEliminar.remove();
    }
} 



