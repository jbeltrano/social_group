CREATE TABLE `usuario` (
  `correo` varchar(255) PRIMARY KEY,
  `nombre` varchar(255) NOT NULL,
  `contraseña` varchar(255) NOT NULL
);

CREATE TABLE `receta` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `creacion` date NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `imagen` binary NOT NULL,
  `descripcion` text NOT NULL,
  `ingredientes` text NOT NULL,
  `pasos` text NOT NULL,
  `tiempo` time,
  `porcion` tinyint,
  `calificacion` tinyint,
  `verificacion` bool,
  `correo` varchar(255) NOT NULL
);

CREATE TABLE `calificacion` (
  `id` integer,
  `correo` varchar(255),
  `numero` tinyint NOT NULL,
  `comentario` text,
  `fecha` date NOT NULL,
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
