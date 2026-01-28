// Listado de facturas:
db["facturas"].find()

// Insertar un elemento:
db.facturas.insertOne({
    nombre:"Jose Vicente",
    apellidos:"Carratala",
    telefono:"+34 620891718",
    email:"info@josevicentecarratala.com"
})