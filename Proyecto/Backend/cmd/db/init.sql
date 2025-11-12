PRAGMA foreign_keys = ON;

CREATE TABLE usuario (
  correo TEXT PRIMARY KEY,
  nombre TEXT NOT NULL,
  contrasena TEXT NOT NULL
);

CREATE TABLE receta (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  creacion TEXT NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  nombre TEXT NOT NULL,
  imagen BLOB NOT NULL,
  descripcion TEXT NOT NULL,
  ingredientes TEXT NOT NULL,
  pasos TEXT NOT NULL,
  tiempo TEXT,
  porcion INTEGER,
  calificacion INTEGER DEFAULT 0,
  verificacion INTEGER DEFAULT 0,
  usuario_correo TEXT NOT NULL,
  FOREIGN KEY (usuario_correo) REFERENCES usuario(correo) ON DELETE CASCADE
);

CREATE TABLE calificacion (
  receta_id INTEGER,
  usuario_correo TEXT,
  numero INTEGER NOT NULL,
  comentario TEXT,
  fecha TEXT NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY (receta_id, usuario_correo),
  FOREIGN KEY (usuario_correo) REFERENCES usuario(correo) ON DELETE CASCADE,
  FOREIGN KEY (receta_id) REFERENCES receta(id) ON DELETE CASCADE
);

CREATE TABLE categoria (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL
);

CREATE TABLE receta_categoria (
  receta_id INTEGER,
  categoria_id INTEGER,
  PRIMARY KEY (receta_id, categoria_id),
  FOREIGN KEY (categoria_id) REFERENCES categoria(id) ON DELETE CASCADE,
  FOREIGN KEY (receta_id) REFERENCES receta(id) ON DELETE CASCADE
);

CREATE TABLE favorito (
  receta_id INTEGER,
  usuario_correo TEXT,
  PRIMARY KEY (receta_id, usuario_correo),
  FOREIGN KEY (receta_id) REFERENCES receta(id) ON DELETE CASCADE,
  FOREIGN KEY (usuario_correo) REFERENCES usuario(correo) ON DELETE CASCADE
);

CREATE TABLE "like" (
  receta_id INTEGER,
  usuario_correo TEXT,
  PRIMARY KEY (receta_id, usuario_correo),
  FOREIGN KEY (receta_id) REFERENCES receta(id) ON DELETE CASCADE,
  FOREIGN KEY (usuario_correo) REFERENCES usuario(correo) ON DELETE CASCADE
);

CREATE TABLE usuario_seguidor (
  usuario_seguidor TEXT,
  usuario_seguido TEXT,
  PRIMARY KEY (usuario_seguidor, usuario_seguido),
  FOREIGN KEY (usuario_seguidor) REFERENCES usuario(correo) ON DELETE CASCADE,
  FOREIGN KEY (usuario_seguido) REFERENCES usuario(correo) ON DELETE CASCADE
);

-- Trigger: actualizar calificacion al insertar
CREATE TRIGGER tg_actualizar_calificacion_receta_insert
AFTER INSERT ON calificacion
FOR EACH ROW
BEGIN
  UPDATE receta
  SET calificacion = (
    SELECT ROUND(AVG(numero))
    FROM calificacion
    WHERE receta_id = NEW.receta_id
  )
  WHERE id = NEW.receta_id;
END;

-- Trigger: actualizar calificacion al modificar
CREATE TRIGGER tg_actualizar_calificacion_receta_update
AFTER UPDATE ON calificacion
FOR EACH ROW
BEGIN
  UPDATE receta
  SET calificacion = (
    SELECT ROUND(AVG(numero))
    FROM calificacion
    WHERE receta_id = NEW.receta_id
  )
  WHERE id = NEW.receta_id;
END;

-- Trigger: actualizar fecha al modificar comentario
CREATE TRIGGER tg_actualizar_fecha_comentario
BEFORE UPDATE ON calificacion
FOR EACH ROW
BEGIN
  SET NEW.fecha = CURRENT_TIMESTAMP;
END;

-- Trigger: verificar recetas segun cantidad y promedio
CREATE TRIGGER tg_actualizar_verificacion
AFTER UPDATE ON calificacion
FOR EACH ROW
BEGIN
  UPDATE receta
  SET verificacion = CASE
    WHEN (
      (SELECT COUNT(*) FROM calificacion WHERE receta_id = NEW.receta_id) > 10
      AND
      (SELECT AVG(numero) FROM calificacion WHERE receta_id = NEW.receta_id) > 3
    ) THEN 1
    ELSE 0
  END
  WHERE id = NEW.receta_id;
END;
