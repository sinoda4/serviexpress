$(function () {
    console.log("funcionando");
    if (localStorage.getItem("carrito") == null) {
        console.log("chao");
        let carrito = []
        localStorage.setItem("carrito", JSON.stringify(carrito))
    }
})





$("#btnAddProducto").on("click", function () {
    console.log("holi");
    let carrito = JSON.parse(localStorage.getItem("carrito"))

    console.log(carrito);

    //Obtener valores de html
    let idProducto = $("#idProducto").val()
    console.log(idProducto);
    let nombreProducto= $("#nombreProducto").val()
    console.log(nombreProducto);
    let precioProducto = $("#precioProducto").val()
    console.log(precioProducto);
    let imagenProducto = $("#imagenProducto").val()
    console.log(imagenProducto);
    let cantidadProducto = 1
    

    //Agregar a localstorage
    if (carrito.length == 0) {
        const obj = {
            id_producto: idProducto,
            nombre: nombreProducto,
            precio: precioProducto,
            imagen: imagenProducto,
            cantidad: cantidadProducto,
        }
        carrito.push(obj)
    }
    else {
        let index = carrito.findIndex(object => {
            return object.id_producto === idProducto;
        })
        console.log(index);
        if (index == -1) {
            const obj = {
                id_producto: idProducto,
                nombre: nombreProducto,
                precio: precioProducto,
                imagen: imagenProducto,
                cantidad: cantidadProducto,
            }
            carrito.push(obj)
        }        
        else{
            cantidadActual = carrito[index].cantidad;
            carrito[index] = {
                id_producto: idProducto,
                nombre: nombreProducto,
                precio: precioProducto,
                imagen: imagenProducto,
                cantidad: cantidadActual + cantidadProducto,

            }
        }
        
    }

    localStorage.setItem("carrito", JSON.stringify(carrito));
    
   
})



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