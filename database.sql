CREATE DATABASE servicio_social;

USE servicio_social;

CREATE TABLE eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion TEXT,
    fecha DATE,
    hora TIME,
    lugar VARCHAR(255),
    tipo_actividad VARCHAR(100)
);

CREATE TABLE registros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT,
    estudiante VARCHAR(255),
    FOREIGN KEY (id_evento) REFERENCES eventos(id)
);
