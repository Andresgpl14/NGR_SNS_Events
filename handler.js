module.exports.process_sns = (event, context) => {
    console.log("**Ingreso de NODEJS process_sns**")
    console.log("event::"+JSON.stringify(event));

    const response = {
        statusCode: 200,
        body: JSON.stringify({
          message: `Mensaje procesado`,
        }),
      };
  
      return response; // Retornamos el objeto que AWS usará como respuesta
};