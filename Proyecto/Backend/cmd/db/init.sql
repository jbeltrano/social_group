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
  `id` integer,
  `correo` varchar(255),
  `numero` tinyint NOT NULL,
  `comentario` text,
  `fecha` date NOT NULL DEFAULT (now()),
  PRIMARY KEY (`id`, `correo`)
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

ALTER TABLE `receta` ADD FOREIGN KEY (`usuario_correo`) REFERENCES `usuario` (`correo`);

ALTER TABLE `calificacion` ADD FOREIGN KEY (`correo`) REFERENCES `usuario` (`correo`);

ALTER TABLE `calificacion` ADD FOREIGN KEY (`id`) REFERENCES `receta` (`id`);

ALTER TABLE `receta_categoria` ADD FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`id`);

ALTER TABLE `receta_categoria` ADD FOREIGN KEY (`receta_id`) REFERENCES `receta` (`id`);

ALTER TABLE `favorito` ADD FOREIGN KEY (`receta_id`) REFERENCES `receta` (`id`);

ALTER TABLE `favorito` ADD FOREIGN KEY (`usuario_correo`) REFERENCES `usuario` (`correo`);

ALTER TABLE `like` ADD FOREIGN KEY (`receta_id`) REFERENCES `receta` (`id`);

ALTER TABLE `like` ADD FOREIGN KEY (`usuario_correo`) REFERENCES `usuario` (`correo`);

ALTER TABLE `usuario_seguidor` ADD FOREIGN KEY (`usuario_seguido`) REFERENCES `usuario` (`correo`);

ALTER TABLE `usuario_seguidor` ADD FOREIGN KEY (`usuario_seguidor`) REFERENCES `usuario` (`correo`);
