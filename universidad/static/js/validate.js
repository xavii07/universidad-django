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

$("#form-curso").validate({
  rules: {
    nivel_cur: {
      required: true,
      maxlength: 50,
    },
    aula_cur: {
      required: true,
      digits: true,
    },
    fk_id_car: {
      required: true,
    },
  },
  messages: {
    nivel_cur: {
      required: "Nivel es obligatorio",
      maxlength: "Maximo caracteres 50",
    },
    aula_cur: {
      required: "Aula obligatoria",
      digits: "Solamente numeros",
    },
    fk_id_car: {
      required: "Carrera obligatoria",
    },
  },
});

$("#form-materia").validate({
  rules: {
    nombre_mat: {
      required: true,
      maxlength: 50,
    },
    creditos_mat: {
      required: true,
      digits: true,
    },
    silabo_mat: {
      required: true,
    },
    fk_id_cur: {
      required: true,
    },
  },
  messages: {
    nombre_mat: {
      required: "Nombre es obligatorio",
      maxlength: "Maximo caracteres 50",
    },
    creditos_mat: {
      required: "Creditos obligatoria",
      digits: "Solamente numeros",
    },
    silabo_mat: {
      required: "Silabo obligatoria",
    },
    fk_id_cur: {
      required: "Curso obligatorio",
    },
  },
});
