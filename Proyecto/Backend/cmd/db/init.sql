CREATE TABLE `usuario` (
  `correo` varchar(255) PRIMARY KEY,
  `nombre` varchar(255) NOT NULL,
  `contrasena` varchar(255) NOT NULL
);

CREATE TABLE `receta` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `creacion` DATE NOT NULL DEFAULT CURRENT_DATE,
  `nombre` VARCHAR(255) NOT NULL,
  `imagen` BLOB NOT NULL,
  `descripcion` TEXT NOT NULL,
  `ingredientes` TEXT NOT NULL,
  `pasos` TEXT NOT NULL,
  `tiempo` TIME,
  `porcion` TINYINT,
  `calificacion` TINYINT,
  `verificacion` BOOL,
  `correo` VARCHAR(255) NOT NULL
);

CREATE TABLE `calificacion` (
  `id` integer,
  `correo` varchar(255),
  `numero` tinyint NOT NULL,
  `comentario` text,
  `fecha` DATE NOT NULL DEFAULT CURRENT_DATE,
  PRIMARY KEY (`id`, `correo`)
);

CREATE TABLE `categoria` (
  `cat_id` integer PRIMARY KEY,
  `nombre` varchar(255) NOT NULL
);

CREATE TABLE `receta_categoria` (
  `id` integer,
  `cat_id` integer,
  PRIMARY KEY (`id`, `cat_id`)
);

CREATE TABLE `favorito` (
  `id` integer,
  `correo` varchar(255),
  PRIMARY KEY (`id`, `correo`)
);

CREATE TABLE `like` (
  `id` integer,
  `correo` varchar(255),
  PRIMARY KEY (`id`, `correo`)
);

CREATE TABLE `usuario_seguidor` (
  `seguidor` varchar(255),
  `seguido` varchar(255),
  PRIMARY KEY (`seguidor`, `seguido`)
);

ALTER TABLE `receta` ADD FOREIGN KEY (`correo`) REFERENCES `usuario` (`correo`);

ALTER TABLE `calificacion` ADD FOREIGN KEY (`correo`) REFERENCES `usuario` (`correo`);

ALTER TABLE `calificacion` ADD FOREIGN KEY (`id`) REFERENCES `receta` (`id`);

ALTER TABLE `receta_categoria` ADD FOREIGN KEY (`cat_id`) REFERENCES `categoria` (`cat_id`);

ALTER TABLE `receta_categoria` ADD FOREIGN KEY (`id`) REFERENCES `receta` (`id`);

ALTER TABLE `favorito` ADD FOREIGN KEY (`id`) REFERENCES `receta` (`id`);

ALTER TABLE `favorito` ADD FOREIGN KEY (`correo`) REFERENCES `usuario` (`correo`);

ALTER TABLE `like` ADD FOREIGN KEY (`id`) REFERENCES `receta` (`id`);

ALTER TABLE `like` ADD FOREIGN KEY (`correo`) REFERENCES `usuario` (`correo`);

ALTER TABLE `usuario_seguidor` ADD FOREIGN KEY (`seguido`) REFERENCES `usuario` (`correo`);

ALTER TABLE `usuario_seguidor` ADD FOREIGN KEY (`seguidor`) REFERENCES `usuario` (`correo`);
