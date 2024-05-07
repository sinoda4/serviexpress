$(function () {
    console.log("hola gente soy inicio");
    let valDolar;
    //consulta api de valor dolar.
    //url
    const apiUrl = 'https://mindicador.cl/api/dolar';

    // Realizar la solicitud GET utilizando fetch
    fetch(apiUrl)
    .then(response => {
        // Verificar si la solicitud fue exitosa (código de estado 200)
        if (response.ok) {
        // Parsear la respuesta a formato JSON
        return response.json();
        } else {
        // En caso de error, lanzar una excepción
        throw new Error('Error al obtener los datos del API');
        }
    })
    .then(data => {
        // Extraer el valor del dólar desde los datos obtenidos
        const valorDolar = data.serie[0].valor;
        valDolar = valorDolar;

        // Mostrar el valor del dólar en la consola
        let htmlElemento = $("#precioDolar").text(valDolar);
        console.log(`El valor del dólar es: $${valorDolar} pesos chilenos`);
    })
    .catch(error => {
        // Capturar y manejar cualquier error que ocurra durante el proceso
        console.error('Ocurrió un error:', error);
    });


    

})    