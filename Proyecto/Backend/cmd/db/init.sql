CREATE TABLE `usuario` (
  `correo` varchar(255) PRIMARY KEY,
  `nombre` varchar(255) NOT NULL,
  `contrasena` varchar(255) NOT NULL
);

CREATE TABLE `receta` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `creacion` date NOT NULL DEFAULT (now()),
  `nombre` varchar(255) NOT NULL,
  `imagen` mediumblob NOT NULL,
  `descripcion` text NOT NULL,
  `ingredientes` text NOT NULL,
  `pasos` text NOT NULL,
  `tiempo` time,
  `porcion` tinyint,
  `calificacion` tinyint DEFAULT 0,
  `verificacion` bool DEFAULT false,
  `usuario_correo` varchar(255) NOT NULL
);

CREATE TABLE `calificacion` (
  `receta_id` integer,
  `usuario_correo` varchar(255),
  `numero` tinyint NOT NULL,
  `comentario` text,
  `fecha` date NOT NULL DEFAULT (now()),
  PRIMARY KEY (`receta_id`, `usuario_correo`)
);

CREATE TABLE `categoria` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL
);

CREATE TABLE `receta_categoria` (
  `receta_id` integer,
  `categoria_id` integer,
  PRIMARY KEY (`receta_id`, `categoria_id`)
);

CREATE TABLE `favorito` (
  `receta_id` integer,
  `usuario_correo` varchar(255),
  PRIMARY KEY (`receta_id`, `usuario_correo`)
);

CREATE TABLE `like` (
  `receta_id` integer,
  `usuario_correo` varchar(255),
  PRIMARY KEY (`receta_id`, `usuario_correo`)
);

CREATE TABLE `usuario_seguidor` (
  `usuario_seguidor` varchar(255),
  `usuario_seguido` varchar(255),
  PRIMARY KEY (`usuario_seguidor`, `usuario_seguido`)
);

ALTER TABLE `receta` ADD FOREIGN KEY (`usuario_correo`) REFERENCES `usuario` (`correo`) ON DELETE CASCADE;

ALTER TABLE `calificacion` ADD FOREIGN KEY (`usuario_correo`) REFERENCES `usuario` (`correo`) ON DELETE CASCADE;

ALTER TABLE `calificacion` ADD FOREIGN KEY (`receta_id`) REFERENCES `receta` (`id`) ON DELETE CASCADE;

ALTER TABLE `receta_categoria` ADD FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`id`) ON DELETE CASCADE;

ALTER TABLE `receta_categoria` ADD FOREIGN KEY (`receta_id`) REFERENCES `receta` (`id`) ON DELETE CASCADE;

ALTER TABLE `favorito` ADD FOREIGN KEY (`receta_id`) REFERENCES `receta` (`id`) ON DELETE CASCADE;

ALTER TABLE `favorito` ADD FOREIGN KEY (`usuario_correo`) REFERENCES `usuario` (`correo`) ON DELETE CASCADE;

ALTER TABLE `like` ADD FOREIGN KEY (`receta_id`) REFERENCES `receta` (`id`) ON DELETE CASCADE;

ALTER TABLE `like` ADD FOREIGN KEY (`usuario_correo`) REFERENCES `usuario` (`correo`) ON DELETE CASCADE;

ALTER TABLE `usuario_seguidor` ADD FOREIGN KEY (`usuario_seguido`) REFERENCES `usuario` (`correo`) ON DELETE CASCADE;

ALTER TABLE `usuario_seguidor` ADD FOREIGN KEY (`usuario_seguidor`) REFERENCES `usuario` (`correo`) ON DELETE CASCADE;



DELIMITER //

CREATE TRIGGER tg_actualizar_calificacion_receta_insert
AFTER INSERT ON calificacion
FOR EACH ROW
BEGIN
    DECLARE nueva_calificacion FLOAT;

    SELECT AVG(numero) INTO nueva_calificacion
    FROM calificacion
    WHERE receta_id = NEW.receta_id;

    UPDATE receta
    SET calificacion = ROUND(nueva_calificacion)
    WHERE id = NEW.receta_id;
END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER tg_actualizar_calificacion_receta_update
AFTER UPDATE ON calificacion
FOR EACH ROW
BEGIN
    DECLARE nueva_calificacion FLOAT;

    SELECT AVG(numero) INTO nueva_calificacion
    FROM calificacion
    WHERE receta_id = NEW.receta_id;

    UPDATE receta
    SET calificacion = ROUND(nueva_calificacion)
    WHERE id = NEW.receta_id;
END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER tg_actualizar_fecha_comentario
BEFORE UPDATE ON calificacion
FOR EACH ROW
BEGIN
    SET NEW.fecha = NOW();
END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER tg_actualizar_verificacion
AFTER UPDATE ON calificacion
FOR EACH ROW
BEGIN
    DECLARE cantidad INT;
    DECLARE promedio FLOAT;

    -- Obtener cantidad de calificaciones de la receta
    SELECT COUNT(*)
    INTO cantidad
    FROM calificacion
    WHERE receta_id = NEW.receta_id;

    -- Obtener promedio de calificación
    SELECT AVG(numero)
    INTO promedio
    FROM calificacion
    WHERE receta_id = NEW.receta_id;

    -- Condición solicitada
    IF cantidad > 10 AND promedio > 3 THEN
        UPDATE receta
        SET verificacion = TRUE
        WHERE id = NEW.receta_id;
    ELSE
        -- (Opcional) Si quieres que vuelva a no verificada cuando no cumple
        UPDATE receta
        SET verificacion = FALSE
        WHERE id = NEW.receta_id;
    END IF;
END //

DELIMITER ;

INSERT INTO categoria (nombre) VALUES
('Entradas'),
('Sopas y Cremas'),
('Ensaladas'),
('Plato Principal'),
('Comida Rápida'),
('Postres y Pasteles'),
('Salsas y aderezos'),
('Panes y masas'),
('Bebidas'),
('Saludables'),
('Vegetariano');