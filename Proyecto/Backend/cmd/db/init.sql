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
  `calificacion` tinyint,
  `verificacion` bool,
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