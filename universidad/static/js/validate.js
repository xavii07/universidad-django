$("#form-carrera").validate({
  rules: {
    nombre_car: {
      required: true,
      maxlength: 50,
    },
    fecha_creacion_car: {
      required: true,
    },
    telefono_car: {
      required: true,
    },
  },
  messages: {
    nombre_car: {
      required: "Nombre carrera es obligatorio",
      maxlength: "Maximo caracteres 50",
    },
    fecha_creacion_car: {
      required: "Fecha creacion obligatoria",
    },
    telefono_car: {
      required: "Telefono obligatorio",
    },
  },
});
