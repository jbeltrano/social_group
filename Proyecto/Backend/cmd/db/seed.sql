-- datos de prueba generados Claude 3.5
INSERT INTO usuario VALUES
('jbeltrano@unal.edu.co', 'Juan David Beltran Orjuela', '11234'),
('fernando@gmail.com', 'Fernando Perez Gomez', 'abcd1234');

-- Insertar categorías
INSERT INTO categoria (nombre) VALUES
('Desayunos'),
('Comida Mexicana'),
('Postres'),
('Comida Italiana'),
('Comida Rápida'),
('Saludable'),
('Vegetariana');

-- Insertar recetas (usando UNHEX para simular datos binarios de imagen)
INSERT INTO receta (nombre, imagen, descripcion, ingredientes, pasos, tiempo, porcion, verificacion, usuario_correo) VALUES
('Pizza Casera', UNHEX('89504E470D0A1A0A'), 'Una deliciosa pizza casera con masa crujiente', 
'- 300g harina\n- 200ml agua\n- 15g levadura\n- Sal\n- Salsa de tomate\n- Queso mozzarella\n- Pepperoni',
'1. Preparar la masa\n2. Dejar reposar 1 hora\n3. Estirar\n4. Añadir ingredientes\n5. Hornear a 200°C',
'01:30:00', 4, true, 'fernando@gmail.com'),

('Tacos al Pastor', UNHEX('89504E470D0A1A0A'), 'Auténticos tacos al pastor mexicanos', 
'- Carne de cerdo\n- Achiote\n- Piña\n- Tortillas\n- Cebolla\n- Cilantro',
'1. Marinar la carne\n2. Cocinar en trompo\n3. Cortar en tiras\n4. Servir en tortillas\n5. Decorar',
'02:00:00', 6, true, 'jbeltrano@unal.edu.co'),

('Tiramisú', UNHEX('89504E470D0A1A0A'), 'Clásico postre italiano', 
'- Café\n- Bizcochos\n- Mascarpone\n- Huevos\n- Azúcar\n- Cacao en polvo',
'1. Preparar café\n2. Batir mascarpone\n3. Remojar bizcochos\n4. Armar capas\n5. Refrigerar',
'00:45:00', 8, true, 'fernando@gmail.com'),

('Ensalada César', UNHEX('89504E470D0A1A0A'), 'Ensalada César tradicional', 
'- Lechuga romana\n- Crutones\n- Parmesano\n- Pollo\n- Salsa César',
'1. Cortar lechuga\n2. Cocinar pollo\n3. Preparar salsa\n4. Mezclar ingredientes\n5. Servir',
'00:20:00', 2, true, 'jbeltrano@unal.edu.co');

-- Relacionar recetas con categorías
INSERT INTO receta_categoria (receta_id, categoria_id) VALUES
(1, 4), -- Pizza - Italiana
(1, 5), -- Pizza - Comida Rápida
(2, 2), -- Tacos - Mexicana
(2, 5), -- Tacos - Comida Rápida
(3, 3), -- Tiramisú - Postres
(4, 6), -- Ensalada - Saludable
(4, 7); -- Ensalada - Vegetariana

-- Insertar algunas calificaciones
INSERT INTO calificacion (receta_id, usuario_correo, numero, comentario) VALUES
(1, 'jbeltrano@unal.edu.co', 5, '¡Excelente receta! La masa quedó perfecta.'),
(2, 'fernando@gmail.com', 5, 'Muy buenos tacos, auténtico sabor mexicano.'),
(3, 'jbeltrano@unal.edu.co', 4, 'Muy buen postre, aunque un poco dulce para mi gusto.'),
(4, 'fernando@gmail.com', 5, 'Ensalada fresca y saludable, perfecta para el verano.');

-- Insertar algunos favoritos
INSERT INTO favorito (receta_id, usuario_correo) VALUES
(1, 'jbeltrano@unal.edu.co'),
(2, 'fernando@gmail.com'),
(3, 'jbeltrano@unal.edu.co'),
(4, 'fernando@gmail.com');

-- Insertar algunos likes
INSERT INTO `like` (receta_id, usuario_correo) VALUES
(1, 'jbeltrano@unal.edu.co'),
(1, 'fernando@gmail.com'),
(2, 'fernando@gmail.com'),
(3, 'jbeltrano@unal.edu.co'),
(4, 'fernando@gmail.com');

-- Hacer que los usuarios se sigan entre sí
INSERT INTO usuario_seguidor (usuario_seguidor, usuario_seguido) VALUES
('fernando@gmail.com', 'jbeltrano@unal.edu.co'),
('jbeltrano@unal.edu.co', 'fernando@gmail.com');
