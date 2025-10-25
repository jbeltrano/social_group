-- Datos de prueba generados con chat.gpt-4

-- ========================
-- PARTE 1: RECETAS 1–20
-- ========================

INSERT INTO receta (nombre, imagen, descripcion, ingredientes, pasos, tiempo, porcion, verificacion, usuario_correo) VALUES
('Huevos Rancheros', UNHEX('89504E470D0A1A0A'), 'Desayuno mexicano tradicional con salsa picante.', '- 2 huevos\n- 2 tortillas\n- Salsa de tomate\n- Frijoles refritos\n- Aguacate', '1. Freír las tortillas.\n2. Cocinar los huevos.\n3. Agregar salsa caliente.\n4. Servir con frijoles y aguacate.', '00:25:00', 2, true, 'jbeltrano@unal.edu.co'),
('Panqueques Esponjosos', UNHEX('89504E470D0A1A0A'), 'Clásicos panqueques para un desayuno perfecto.', '- 200g harina\n- 1 huevo\n- 250ml leche\n- 1 cda azúcar\n- Mantequilla', '1. Mezclar los ingredientes.\n2. Cocinar porciones en sartén.\n3. Servir con miel o frutas.', '00:20:00', 3, true, 'fernando@gmail.com'),
('Guacamole Casero', UNHEX('89504E470D0A1A0A'), 'Dip de aguacate fresco y saludable.', '- 2 aguacates\n- Tomate picado\n- Cebolla\n- Limón\n- Sal', '1. Triturar los aguacates.\n2. Mezclar con el resto de ingredientes.\n3. Servir frío.', '00:10:00', 4, true, 'jbeltrano@unal.edu.co'),
('Pasta Alfredo', UNHEX('89504E470D0A1A0A'), 'Cremosa pasta italiana con salsa Alfredo.', '- 250g fettuccine\n- 200ml crema\n- Queso parmesano\n- Mantequilla\n- Ajo', '1. Cocinar la pasta.\n2. Preparar la salsa.\n3. Mezclar y servir caliente.', '00:30:00', 2, true, 'fernando@gmail.com'),
('Smoothie Verde', UNHEX('89504E470D0A1A0A'), 'Batido saludable de espinaca y plátano.', '- Espinaca\n- Plátano\n- Leche vegetal\n- Miel', '1. Licuar todos los ingredientes.\n2. Servir frío.', '00:05:00', 1, true, 'jbeltrano@unal.edu.co'),
('Hamburguesa Casera', UNHEX('89504E470D0A1A0A'), 'Jugosa hamburguesa con pan artesanal.', '- Carne molida\n- Pan de hamburguesa\n- Lechuga\n- Tomate\n- Queso cheddar', '1. Formar hamburguesas.\n2. Cocinar a la parrilla.\n3. Armar y servir.', '00:35:00', 2, true, 'fernando@gmail.com'),
('Chilaquiles Verdes', UNHEX('89504E470D0A1A0A'), 'Plato mexicano de totopos bañados en salsa verde.', '- Totopos\n- Salsa verde\n- Pollo desmenuzado\n- Crema\n- Queso fresco', '1. Calentar la salsa.\n2. Agregar los totopos.\n3. Añadir pollo, crema y queso.', '00:25:00', 2, true, 'jbeltrano@unal.edu.co'),
('Brownies de Chocolate', UNHEX('89504E470D0A1A0A'), 'Brownies húmedos y llenos de sabor a cacao.', '- 200g chocolate\n- 100g mantequilla\n- 2 huevos\n- 100g azúcar\n- 80g harina', '1. Derretir chocolate y mantequilla.\n2. Mezclar con el resto.\n3. Hornear 25 minutos.', '00:45:00', 8, true, 'fernando@gmail.com'),
('Ensalada Mediterránea', UNHEX('89504E470D0A1A0A'), 'Fresca ensalada con ingredientes mediterráneos.', '- Tomates cherry\n- Aceitunas\n- Queso feta\n- Lechuga\n- Aceite de oliva', '1. Cortar y mezclar ingredientes.\n2. Aliñar con aceite de oliva.', '00:15:00', 3, true, 'jbeltrano@unal.edu.co'),
('Fajitas de Pollo', UNHEX('89504E470D0A1A0A'), 'Clásicas fajitas mexicanas con vegetales.', '- Pechuga de pollo\n- Pimientos\n- Cebolla\n- Tortillas\n- Limón', '1. Saltear pollo y vegetales.\n2. Servir en tortillas.\n3. Acompañar con limón.', '00:40:00', 4, true, 'fernando@gmail.com'),
('Muffins de Avena', UNHEX('89504E470D0A1A0A'), 'Muffins saludables con avena y plátano.', '- Avena\n- Plátano\n- Huevo\n- Canela\n- Miel', '1. Mezclar los ingredientes.\n2. Hornear 20 minutos.', '00:30:00', 6, true, 'jbeltrano@unal.edu.co'),
('Lasaña Boloñesa', UNHEX('89504E470D0A1A0A'), 'Lasaña tradicional italiana con carne y salsa.', '- Láminas de pasta\n- Carne molida\n- Salsa boloñesa\n- Queso\n- Bechamel', '1. Preparar la salsa.\n2. Armar capas.\n3. Hornear 40 minutos.', '01:30:00', 6, true, 'fernando@gmail.com'),
('Quesadillas de Queso', UNHEX('89504E470D0A1A0A'), 'Rápidas y deliciosas quesadillas mexicanas.', '- Tortillas\n- Queso Oaxaca\n- Guacamole\n- Salsa', '1. Rellenar tortillas.\n2. Calentar hasta derretir el queso.\n3. Servir con guacamole.', '00:15:00', 2, true, 'jbeltrano@unal.edu.co'),
('Tostadas Francesas', UNHEX('89504E470D0A1A0A'), 'Dulce desayuno con pan, huevo y canela.', '- Pan\n- Huevo\n- Leche\n- Azúcar\n- Canela', '1. Batir huevo y leche.\n2. Remojar pan.\n3. Cocinar en sartén.', '00:20:00', 2, true, 'fernando@gmail.com'),
('Gazpacho Andaluz', UNHEX('89504E470D0A1A0A'), 'Sopa fría saludable a base de tomate.', '- Tomate\n- Pimiento\n- Pepino\n- Ajo\n- Aceite de oliva', '1. Licuar todos los ingredientes.\n2. Servir frío.', '00:15:00', 3, true, 'jbeltrano@unal.edu.co'),
('Pizza Margarita', UNHEX('89504E470D0A1A0A'), 'Pizza italiana clásica con tomate y albahaca.', '- Masa para pizza\n- Salsa de tomate\n- Queso mozzarella\n- Albahaca fresca', '1. Preparar la masa.\n2. Añadir ingredientes.\n3. Hornear 20 minutos.', '01:00:00', 4, true, 'fernando@gmail.com'),
('Crepas Dulces', UNHEX('89504E470D0A1A0A'), 'Deliciosas crepas para postre o desayuno.', '- Harina\n- Huevo\n- Leche\n- Azúcar\n- Frutas', '1. Mezclar masa.\n2. Cocinar finas crepas.\n3. Rellenar y servir.', '00:25:00', 3, true, 'jbeltrano@unal.edu.co'),
('Wrap Vegetariano', UNHEX('89504E470D0A1A0A'), 'Envoltura saludable con verduras frescas.', '- Tortilla integral\n- Hummus\n- Lechuga\n- Tomate\n- Zanahoria rallada', '1. Extender hummus.\n2. Agregar verduras.\n3. Enrollar y cortar.', '00:10:00', 1, true, 'fernando@gmail.com'),
('Cupcakes de Vainilla', UNHEX('89504E470D0A1A0A'), 'Pequeños pastelitos suaves y esponjosos.', '- Harina\n- Huevo\n- Leche\n- Azúcar\n- Vainilla', '1. Mezclar ingredientes.\n2. Hornear 20 minutos.', '00:35:00', 12, true, 'jbeltrano@unal.edu.co'),
('Sopa de Lentejas', UNHEX('89504E470D0A1A0A'), 'Sopa nutritiva y reconfortante.', '- Lentejas\n- Zanahoria\n- Cebolla\n- Tomate\n- Caldo', '1. Cocinar verduras.\n2. Agregar lentejas.\n3. Hervir 40 minutos.', '01:00:00', 4, true, 'fernando@gmail.com');

-- Categorías asociadas (ids de categoría del ejemplo original)
INSERT INTO receta_categoria (receta_id, categoria_id) VALUES
(5, 1), (5, 2),
(6, 1), (6, 6),
(7, 2), (7, 6),
(8, 4), (8, 5),
(9, 6), (9, 7),
(10, 5), (10, 2),
(11, 3), (11, 7),
(12, 4),
(13, 2), (13, 5),
(14, 1), (14, 3),
(15, 6), (15, 7),
(16, 4), (16, 5),
(17, 1), (17, 3),
(18, 6), (18, 7),
(19, 3),
(20, 6), (20, 7),
(21, 3), (21, 5),
(22, 6);


-- ========================
-- PARTE 2: RECETAS 21–40
-- ========================

INSERT INTO receta (nombre, imagen, descripcion, ingredientes, pasos, tiempo, porcion, verificacion, usuario_correo) VALUES
('Enchiladas Rojas', UNHEX('89504E470D0A1A0A'), 'Enchiladas mexicanas bañadas en salsa roja.', '- Tortillas\n- Pollo desmenuzado\n- Salsa roja\n- Crema\n- Queso fresco', '1. Rellenar las tortillas con pollo.\n2. Bañar en salsa roja.\n3. Hornear 10 minutos.\n4. Servir con crema y queso.', '00:45:00', 4, true, 'jbeltrano@unal.edu.co'),
('Risotto de Champiñones', UNHEX('89504E470D0A1A0A'), 'Cremoso risotto italiano con setas frescas.', '- Arroz arborio\n- Champiñones\n- Caldo de verduras\n- Queso parmesano', '1. Sofreír los champiñones.\n2. Agregar arroz y caldo.\n3. Cocinar lentamente.\n4. Añadir parmesano.', '01:10:00', 3, true, 'fernando@gmail.com'),
('Tostadas de Aguacate', UNHEX('89504E470D0A1A0A'), 'Desayuno saludable y fácil con pan integral.', '- Pan integral\n- Aguacate\n- Tomate\n- Limón\n- Sal y pimienta', '1. Tostar pan.\n2. Aplastar aguacate.\n3. Colocar encima con tomate y condimentos.', '00:10:00', 2, true, 'jbeltrano@unal.edu.co'),
('Canelones de Espinaca', UNHEX('89504E470D0A1A0A'), 'Canelones rellenos con espinaca y ricotta.', '- Láminas de pasta\n- Espinaca\n- Ricotta\n- Salsa de tomate\n- Queso', '1. Preparar relleno.\n2. Enrollar canelones.\n3. Cubrir con salsa y hornear.', '01:15:00', 4, true, 'fernando@gmail.com'),
('Sándwich de Pollo', UNHEX('89504E470D0A1A0A'), 'Rápido sándwich con pollo a la plancha.', '- Pan de molde\n- Pollo\n- Lechuga\n- Tomate\n- Mayonesa', '1. Cocinar el pollo.\n2. Armar el sándwich.\n3. Servir con papas o ensalada.', '00:20:00', 1, true, 'jbeltrano@unal.edu.co'),
('Tarta de Manzana', UNHEX('89504E470D0A1A0A'), 'Tarta dulce con manzanas caramelizadas.', '- Manzanas\n- Harina\n- Mantequilla\n- Azúcar\n- Canela', '1. Preparar masa.\n2. Añadir relleno.\n3. Hornear 40 minutos.', '01:10:00', 8, true, 'fernando@gmail.com'),
('Pozole Blanco', UNHEX('89504E470D0A1A0A'), 'Sopa tradicional mexicana de maíz y carne.', '- Maíz pozolero\n- Pollo o cerdo\n- Lechuga\n- Rábano\n- Limón', '1. Cocinar el maíz.\n2. Agregar carne.\n3. Servir con guarniciones.', '02:30:00', 6, true, 'jbeltrano@unal.edu.co'),
('Espaguetis Carbonara', UNHEX('89504E470D0A1A0A'), 'Pasta italiana con huevo y panceta.', '- Espaguetis\n- Panceta\n- Huevo\n- Queso parmesano\n- Pimienta negra', '1. Cocinar pasta.\n2. Freír panceta.\n3. Mezclar con huevo y queso.', '00:35:00', 3, true, 'fernando@gmail.com'),
('Ensalada de Quinoa', UNHEX('89504E470D0A1A0A'), 'Ensalada nutritiva con quinoa y vegetales.', '- Quinoa\n- Tomate\n- Pepino\n- Limón\n- Aceite de oliva', '1. Cocinar quinoa.\n2. Mezclar con verduras y aderezo.', '00:25:00', 2, true, 'jbeltrano@unal.edu.co'),
('Calzone Napolitano', UNHEX('89504E470D0A1A0A'), 'Calzone relleno de jamón y queso al estilo italiano.', '- Masa de pizza\n- Jamón\n- Queso mozzarella\n- Salsa de tomate', '1. Rellenar masa.\n2. Doblar y sellar.\n3. Hornear 25 minutos.', '01:00:00', 2, true, 'fernando@gmail.com'),
('Ensalada de Frutas Tropicales', UNHEX('89504E470D0A1A0A'), 'Mezcla fresca y colorida de frutas tropicales.', '- Piña\n- Mango\n- Papaya\n- Kiwi\n- Miel', '1. Cortar las frutas.\n2. Mezclar y refrigerar.\n3. Servir fría.', '00:10:00', 4, true, 'jbeltrano@unal.edu.co'),
('Burritos de Frijoles', UNHEX('89504E470D0A1A0A'), 'Deliciosos burritos vegetarianos con frijoles.', '- Tortillas\n- Frijoles negros\n- Arroz\n- Queso\n- Salsa', '1. Rellenar las tortillas.\n2. Enrollar.\n3. Calentar en sartén.', '00:30:00', 3, true, 'fernando@gmail.com'),
('Pancitos Integrales', UNHEX('89504E470D0A1A0A'), 'Panecillos caseros con harina integral.', '- Harina integral\n- Levadura\n- Agua\n- Aceite de oliva\n- Sal', '1. Amasar.\n2. Reposar.\n3. Hornear 25 minutos.', '01:20:00', 8, true, 'jbeltrano@unal.edu.co'),
('Canelones de Carne', UNHEX('89504E470D0A1A0A'), 'Canelones clásicos con relleno de carne.', '- Pasta para canelones\n- Carne molida\n- Salsa de tomate\n- Queso', '1. Preparar relleno.\n2. Enrollar y cubrir con salsa.\n3. Hornear.', '01:10:00', 4, true, 'fernando@gmail.com'),
('Tostadas de Atún', UNHEX('89504E470D0A1A0A'), 'Tostadas frías con ensalada de atún y mayonesa.', '- Tostadas\n- Atún\n- Cebolla\n- Mayonesa\n- Limón', '1. Mezclar ingredientes.\n2. Servir sobre tostadas.', '00:15:00', 2, true, 'jbeltrano@unal.edu.co'),
('Gelatina de Yogur y Frutas', UNHEX('89504E470D0A1A0A'), 'Postre fresco y bajo en calorías.', '- Yogur natural\n- Frutas\n- Gelatina sin sabor\n- Miel', '1. Mezclar yogur y gelatina.\n2. Añadir frutas.\n3. Refrigerar.', '00:20:00', 6, true, 'fernando@gmail.com'),
('Tacos de Pescado', UNHEX('89504E470D0A1A0A'), 'Tacos frescos con pescado empanizado.', '- Filetes de pescado\n- Harina\n- Cerveza\n- Tortillas\n- Salsa de col', '1. Rebozar pescado.\n2. Freír.\n3. Servir en tortillas con salsa.', '00:40:00', 4, true, 'jbeltrano@unal.edu.co'),
('Bruschetta Italiana', UNHEX('89504E470D0A1A0A'), 'Entrante italiano con pan tostado y tomate.', '- Pan\n- Tomate\n- Albahaca\n- Aceite de oliva\n- Ajo', '1. Tostar pan.\n2. Añadir mezcla de tomate y albahaca.\n3. Servir.', '00:15:00', 3, true, 'fernando@gmail.com'),
('Waffles de Avena', UNHEX('89504E470D0A1A0A'), 'Desayuno ligero con avena y miel.', '- Avena\n- Huevo\n- Leche\n- Miel\n- Canela', '1. Mezclar ingredientes.\n2. Cocinar en waflera.\n3. Servir con frutas.', '00:25:00', 2, true, 'jbeltrano@unal.edu.co'),
('Macarrones con Queso', UNHEX('89504E470D0A1A0A'), 'Comida rápida cremosa y reconfortante.', '- Pasta corta\n- Queso cheddar\n- Leche\n- Mantequilla\n- Harina', '1. Cocinar la pasta.\n2. Preparar salsa de queso.\n3. Mezclar y servir.', '00:30:00', 3, true, 'fernando@gmail.com');

-- Categorías asociadas
INSERT INTO receta_categoria (receta_id, categoria_id) VALUES
(23, 2), (23, 5),
(24, 4),
(25, 1), (25, 6),
(26, 4), (26, 7),
(27, 5), (27, 6),
(28, 3),
(29, 2), (29, 6),
(30, 4),
(31, 6), (31, 7),
(32, 4), (32, 5),
(33, 3), (33, 6),
(34, 2), (34, 7),
(35, 4), (35, 5),
(36, 2),
(37, 4), (37, 6),
(38, 1), (38, 3),
(39, 2), (39, 5),
(40, 4), (40, 5);


-- ========================
-- PARTE 3: RECETAS 41–60
-- ========================

INSERT INTO receta (nombre, imagen, descripcion, ingredientes, pasos, tiempo, porcion, verificacion, usuario_correo) VALUES
('Chiles Rellenos', UNHEX('89504E470D0A1A0A'), 'Tradicionales chiles poblanos rellenos de queso.', '- Chiles poblanos\n- Queso\n- Huevo\n- Harina\n- Salsa de tomate', '1. Asar y pelar los chiles.\n2. Rellenar con queso.\n3. Empanizar y freír.\n4. Servir con salsa.', '01:10:00', 4, true, 'jbeltrano@unal.edu.co'),
('Raviolis de Ricotta', UNHEX('89504E470D0A1A0A'), 'Raviolis italianos rellenos con ricotta y espinaca.', '- Masa para pasta\n- Ricotta\n- Espinaca\n- Salsa de tomate\n- Queso parmesano', '1. Preparar el relleno.\n2. Armar raviolis.\n3. Cocinar y servir con salsa.', '01:20:00', 3, true, 'fernando@gmail.com'),
('Omelette de Verduras', UNHEX('89504E470D0A1A0A'), 'Desayuno saludable y ligero.', '- Huevos\n- Espinaca\n- Cebolla\n- Tomate\n- Queso', '1. Batir huevos.\n2. Añadir verduras.\n3. Cocinar en sartén.', '00:15:00', 1, true, 'jbeltrano@unal.edu.co'),
('Pollo a la Parmesana', UNHEX('89504E470D0A1A0A'), 'Clásico plato italiano con pollo empanizado y salsa.', '- Pechugas de pollo\n- Pan rallado\n- Salsa de tomate\n- Queso mozzarella', '1. Empanizar pollo.\n2. Freír.\n3. Hornear con salsa y queso.', '01:00:00', 4, true, 'fernando@gmail.com'),
('Tostadas de Huevo y Espinaca', UNHEX('89504E470D0A1A0A'), 'Tostadas saludables con huevo pochado.', '- Pan integral\n- Huevo\n- Espinaca\n- Aceite de oliva\n- Sal', '1. Cocinar espinaca.\n2. Preparar huevo pochado.\n3. Servir sobre pan.', '00:20:00', 2, true, 'jbeltrano@unal.edu.co'),
('Pasta al Pesto', UNHEX('89504E470D0A1A0A'), 'Pasta italiana con salsa de albahaca y nueces.', '- Pasta\n- Albahaca\n- Aceite de oliva\n- Queso parmesano\n- Nueces', '1. Preparar pesto.\n2. Cocinar pasta.\n3. Mezclar y servir.', '00:35:00', 2, true, 'fernando@gmail.com'),
('Nachos con Guacamole', UNHEX('89504E470D0A1A0A'), 'Botana mexicana con totopos y guacamole.', '- Totopos\n- Aguacate\n- Tomate\n- Limón\n- Cilantro', '1. Preparar guacamole.\n2. Servir con totopos.', '00:10:00', 4, true, 'jbeltrano@unal.edu.co'),
('Galletas de Avena', UNHEX('89504E470D0A1A0A'), 'Galletas suaves y saludables con avena y miel.', '- Avena\n- Harina\n- Huevo\n- Miel\n- Canela', '1. Mezclar ingredientes.\n2. Formar galletas.\n3. Hornear 15 minutos.', '00:30:00', 12, true, 'fernando@gmail.com'),
('Tostadas de Pollo', UNHEX('89504E470D0A1A0A'), 'Crujientes tostadas mexicanas con pollo.', '- Tostadas\n- Pollo desmenuzado\n- Lechuga\n- Crema\n- Salsa', '1. Armar tostadas.\n2. Decorar con crema y salsa.', '00:25:00', 3, true, 'jbeltrano@unal.edu.co'),
('Pasta a la Boloñesa Vegetariana', UNHEX('89504E470D0A1A0A'), 'Versión vegetariana del clásico boloñés.', '- Pasta\n- Lentejas\n- Tomate\n- Cebolla\n- Ajo', '1. Cocinar lentejas.\n2. Preparar salsa.\n3. Mezclar con la pasta.', '00:45:00', 3, true, 'fernando@gmail.com'),
('Churros Caseros', UNHEX('89504E470D0A1A0A'), 'Churros crujientes con azúcar y canela.', '- Harina\n- Agua\n- Aceite\n- Azúcar\n- Canela', '1. Preparar masa.\n2. Freír churros.\n3. Rebozar en azúcar y canela.', '00:40:00', 6, true, 'jbeltrano@unal.edu.co'),
('Risotto de Calabaza', UNHEX('89504E470D0A1A0A'), 'Cremoso risotto con calabaza y parmesano.', '- Arroz arborio\n- Calabaza\n- Caldo de verduras\n- Queso parmesano', '1. Cocinar calabaza.\n2. Añadir arroz y caldo poco a poco.\n3. Incorporar parmesano.', '01:15:00', 3, true, 'fernando@gmail.com'),
('Tacos de Nopal', UNHEX('89504E470D0A1A0A'), 'Tacos vegetarianos con nopal asado.', '- Nopales\n- Tortillas\n- Cebolla\n- Cilantro\n- Salsa verde', '1. Asar nopales.\n2. Servir en tortillas con guarniciones.', '00:25:00', 2, true, 'jbeltrano@unal.edu.co'),
('Pan de Plátano', UNHEX('89504E470D0A1A0A'), 'Pan dulce y esponjoso con plátano maduro.', '- Plátanos maduros\n- Harina\n- Huevo\n- Azúcar\n- Aceite', '1. Mezclar ingredientes.\n2. Hornear 40 minutos.', '01:00:00', 8, true, 'fernando@gmail.com'),
('Tacos de Camarón', UNHEX('89504E470D0A1A0A'), 'Tacos frescos con camarones al ajillo.', '- Camarones\n- Tortillas\n- Ajo\n- Limón\n- Aguacate', '1. Cocinar camarones.\n2. Servir con tortillas y guarnición.', '00:30:00', 4, true, 'jbeltrano@unal.edu.co'),
('Espaguetis con Tomate y Albahaca', UNHEX('89504E470D0A1A0A'), 'Pasta ligera y sabrosa con ingredientes frescos.', '- Espaguetis\n- Tomate\n- Albahaca\n- Ajo\n- Aceite de oliva', '1. Cocinar la pasta.\n2. Preparar salsa fresca.\n3. Mezclar y servir.', '00:35:00', 2, true, 'fernando@gmail.com'),
('Tacos Dorados de Papa', UNHEX('89504E470D0A1A0A'), 'Crujientes tacos fritos rellenos de papa.', '- Tortillas\n- Papa cocida\n- Crema\n- Lechuga\n- Salsa roja', '1. Rellenar tortillas con papa.\n2. Freír.\n3. Servir con crema y salsa.', '00:40:00', 4, true, 'jbeltrano@unal.edu.co'),
('Raviolis de Carne', UNHEX('89504E470D0A1A0A'), 'Raviolis rellenos de carne y bañados en salsa boloñesa.', '- Masa de pasta\n- Carne molida\n- Salsa de tomate\n- Queso parmesano', '1. Preparar relleno.\n2. Armar raviolis.\n3. Cocinar y servir.', '01:15:00', 4, true, 'fernando@gmail.com'),
('Panqueques de Avena y Miel', UNHEX('89504E470D0A1A0A'), 'Panqueques saludables y dulces.', '- Avena\n- Huevo\n- Leche\n- Miel\n- Canela', '1. Mezclar ingredientes.\n2. Cocinar en sartén.\n3. Servir con miel.', '00:25:00', 2, true, 'jbeltrano@unal.edu.co'),
('Pasta con Salsa Rosa', UNHEX('89504E470D0A1A0A'), 'Pasta cremosa con mezcla de salsa de tomate y crema.', '- Pasta\n- Salsa de tomate\n- Crema\n- Queso\n- Albahaca', '1. Cocinar pasta.\n2. Preparar salsa.\n3. Mezclar y servir.', '00:40:00', 3, true, 'fernando@gmail.com');

-- Categorías asociadas
INSERT INTO receta_categoria (receta_id, categoria_id) VALUES
(41, 2),
(42, 4),
(43, 1), (43, 6),
(44, 4),
(45, 1), (45, 6),
(46, 4), (46, 7),
(47, 2), (47, 5),
(48, 3), (48, 6),
(49, 2), (49, 5),
(50, 4), (50, 7),
(51, 3),
(52, 4), (52, 7),
(53, 2), (53, 7),
(54, 3), (54, 6),
(55, 2), (55, 5),
(56, 4),
(57, 1), (57, 6),
(58, 4), (58, 5);


-- ========================
-- PARTE 4: RECETAS 61–80
-- ========================

INSERT INTO receta (nombre, imagen, descripcion, ingredientes, pasos, tiempo, porcion, verificacion, usuario_correo) VALUES
('Enchiladas Verdes', UNHEX('89504E470D0A1A0A'), 'Tortillas rellenas de pollo bañadas en salsa verde.', '- Tortillas\n- Pollo desmenuzado\n- Salsa verde\n- Queso fresco\n- Crema', '1. Rellenar las tortillas.\n2. Bañar en salsa.\n3. Hornear 10 minutos.\n4. Servir con crema y queso.', '00:45:00', 4, true, 'jbeltrano@unal.edu.co'),
('Spaghetti al Limón', UNHEX('89504E470D0A1A0A'), 'Pasta italiana ligera con un toque cítrico.', '- Spaghetti\n- Limón\n- Crema\n- Queso parmesano\n- Mantequilla', '1. Cocinar pasta.\n2. Preparar salsa con limón y crema.\n3. Mezclar y servir.', '00:35:00', 2, true, 'fernando@gmail.com'),
('Huevos a la Mexicana', UNHEX('89504E470D0A1A0A'), 'Huevos revueltos con jitomate, cebolla y chile.', '- Huevos\n- Tomate\n- Cebolla\n- Chile\n- Aceite', '1. Picar los ingredientes.\n2. Sofreír.\n3. Agregar los huevos y revolver.', '00:15:00', 2, true, 'jbeltrano@unal.edu.co'),
('Raviolis de Calabaza', UNHEX('89504E470D0A1A0A'), 'Raviolis dulzones rellenos de calabaza.', '- Masa de pasta\n- Calabaza\n- Queso ricotta\n- Mantequilla\n- Salvia', '1. Preparar el relleno.\n2. Armar raviolis.\n3. Servir con mantequilla dorada.', '01:10:00', 3, true, 'fernando@gmail.com'),
('Avena Nocturna', UNHEX('89504E470D0A1A0A'), 'Desayuno saludable que se prepara la noche anterior.', '- Avena\n- Leche vegetal\n- Frutas\n- Miel\n- Semillas', '1. Mezclar ingredientes en frasco.\n2. Refrigerar toda la noche.\n3. Servir fría.', '00:05:00', 1, true, 'jbeltrano@unal.edu.co'),
('Pizza Cuatro Quesos', UNHEX('89504E470D0A1A0A'), 'Pizza italiana con mezcla de cuatro quesos.', '- Masa para pizza\n- Mozzarella\n- Gorgonzola\n- Parmesano\n- Provolone', '1. Preparar masa.\n2. Agregar quesos.\n3. Hornear 20 minutos.', '01:00:00', 4, true, 'fernando@gmail.com'),
('Sopes Mexicanos', UNHEX('89504E470D0A1A0A'), 'Pequeñas tortillas gruesas con frijoles y carne.', '- Masa de maíz\n- Frijoles refritos\n- Pollo o carne\n- Lechuga\n- Salsa', '1. Formar sopes.\n2. Freír.\n3. Añadir toppings.', '00:40:00', 6, true, 'jbeltrano@unal.edu.co'),
('Lasaña Vegetariana', UNHEX('89504E470D0A1A0A'), 'Lasaña con verduras y salsa bechamel.', '- Láminas de pasta\n- Calabacín\n- Berenjena\n- Bechamel\n- Queso', '1. Asar verduras.\n2. Armar capas.\n3. Hornear 40 minutos.', '01:20:00', 6, true, 'fernando@gmail.com'),
('Molletes Mexicanos', UNHEX('89504E470D0A1A0A'), 'Pan con frijoles, queso y pico de gallo.', '- Bolillos\n- Frijoles refritos\n- Queso\n- Pico de gallo', '1. Untar frijoles.\n2. Añadir queso.\n3. Gratinar y servir.', '00:25:00', 2, true, 'jbeltrano@unal.edu.co'),
('Focaccia Italiana', UNHEX('89504E470D0A1A0A'), 'Pan plano italiano con hierbas y aceite de oliva.', '- Harina\n- Aceite de oliva\n- Romero\n- Sal marina\n- Levadura', '1. Amasar masa.\n2. Reposar.\n3. Hornear 30 minutos.', '01:30:00', 8, true, 'fernando@gmail.com'),
('Açai Bowl', UNHEX('89504E470D0A1A0A'), 'Desayuno antioxidante y energético.', '- Pulpa de açai\n- Frutas\n- Granola\n- Miel', '1. Licuar açai con frutas.\n2. Servir con toppings.', '00:10:00', 1, true, 'jbeltrano@unal.edu.co'),
('Pasta con Mariscos', UNHEX('89504E470D0A1A0A'), 'Pasta italiana con camarones y calamares.', '- Pasta\n- Camarones\n- Calamares\n- Ajo\n- Tomate', '1. Sofreír mariscos.\n2. Agregar salsa.\n3. Mezclar con pasta.', '00:50:00', 4, true, 'fernando@gmail.com'),
('Tacos de Pollo con Mango', UNHEX('89504E470D0A1A0A'), 'Tacos frescos con salsa de mango.', '- Pollo\n- Tortillas\n- Mango\n- Cebolla morada\n- Limón', '1. Cocinar pollo.\n2. Preparar salsa.\n3. Servir en tortillas.', '00:35:00', 3, true, 'jbeltrano@unal.edu.co'),
('Risotto de Espárragos', UNHEX('89504E470D0A1A0A'), 'Risotto cremoso con espárragos frescos.', '- Arroz arborio\n- Espárragos\n- Caldo\n- Queso parmesano', '1. Cocinar arroz.\n2. Añadir espárragos.\n3. Servir con queso.', '01:10:00', 3, true, 'fernando@gmail.com'),
('Tamales Mexicanos', UNHEX('89504E470D0A1A0A'), 'Tamales tradicionales con masa y relleno.', '- Masa de maíz\n- Pollo o cerdo\n- Salsa roja\n- Hojas de maíz', '1. Rellenar hojas.\n2. Cocer al vapor.\n3. Servir calientes.', '02:00:00', 6, true, 'jbeltrano@unal.edu.co'),
('Pasta al Horno', UNHEX('89504E470D0A1A0A'), 'Pasta gratinada con salsa y queso.', '- Pasta\n- Salsa de tomate\n- Queso mozzarella\n- Bechamel', '1. Mezclar pasta con salsa.\n2. Cubrir con queso.\n3. Hornear.', '00:55:00', 5, true, 'fernando@gmail.com'),
('Bowl de Garbanzos', UNHEX('89504E470D0A1A0A'), 'Plato saludable con garbanzos y vegetales.', '- Garbanzos\n- Espinaca\n- Tomate\n- Aguacate\n- Limón', '1. Mezclar todos los ingredientes.\n2. Servir con aderezo.', '00:15:00', 2, true, 'jbeltrano@unal.edu.co'),
('Raviolis de Setas', UNHEX('89504E470D0A1A0A'), 'Raviolis rellenos con champiñones salteados.', '- Masa para pasta\n- Champiñones\n- Ajo\n- Queso ricotta', '1. Preparar relleno.\n2. Cocinar raviolis.\n3. Servir con mantequilla.', '01:10:00', 4, true, 'fernando@gmail.com'),
('Sopa Azteca', UNHEX('89504E470D0A1A0A'), 'Sopa mexicana con tiras de tortilla y chile.', '- Tortillas\n- Caldo de pollo\n- Chile pasilla\n- Queso\n- Aguacate', '1. Freír tortillas.\n2. Agregar caldo y chile.\n3. Servir con aguacate.', '00:40:00', 4, true, 'jbeltrano@unal.edu.co'),
('Pasta Primavera', UNHEX('89504E470D0A1A0A'), 'Pasta con verduras frescas de temporada.', '- Pasta\n- Brócoli\n- Zanahoria\n- Pimientos\n- Aceite de oliva', '1. Cocinar pasta.\n2. Saltear verduras.\n3. Mezclar y servir.', '00:35:00', 3, true, 'fernando@gmail.com');

-- Categorías asociadas
INSERT INTO receta_categoria (receta_id, categoria_id) VALUES
(61, 2),
(62, 4),
(63, 1), (63, 2),
(64, 4), (64, 7),
(65, 1), (65, 6),
(66, 4), (66, 5),
(67, 2), (67, 5),
(68, 4), (68, 6), (68, 7),
(69, 2),
(70, 4),
(71, 1), (71, 6),
(72, 4), (72, 5),
(73, 2), (73, 6),
(74, 4), (74, 7),
(75, 2),
(76, 4), (76, 5),
(77, 6), (77, 7),
(78, 4),
(79, 2),
(80, 4), (80, 6);


-- ========================
-- PARTE 5: RECETAS 81–100
-- ========================

INSERT INTO receta (nombre, imagen, descripcion, ingredientes, pasos, tiempo, porcion, verificacion, usuario_correo) VALUES
('Chilaquiles Rojos', UNHEX('89504E470D0A1A0A'), 'Totopos bañados en salsa roja con crema y queso.', '- Totopos\n- Salsa roja\n- Crema\n- Queso fresco\n- Cebolla', '1. Calentar salsa.\n2. Agregar totopos.\n3. Servir con crema y queso.', '00:25:00', 3, true, 'jbeltrano@unal.edu.co'),
('Pasta con Pollo y Champiñones', UNHEX('89504E470D0A1A0A'), 'Pasta cremosa con pollo y champiñones.', '- Pasta\n- Pollo\n- Champiñones\n- Crema\n- Ajo', '1. Cocinar pasta.\n2. Saltear pollo y champiñones.\n3. Agregar crema y mezclar.', '00:45:00', 4, true, 'fernando@gmail.com'),
('Huevos al Horno con Verduras', UNHEX('89504E470D0A1A0A'), 'Desayuno ligero y saludable al horno.', '- Huevos\n- Espinaca\n- Tomate\n- Queso\n- Sal y pimienta', '1. Colocar ingredientes en moldes.\n2. Hornear 12 minutos.', '00:20:00', 2, true, 'jbeltrano@unal.edu.co'),
('Pizza con Jamón y Piña', UNHEX('89504E470D0A1A0A'), 'Pizza hawaiana con sabor dulce y salado.', '- Masa para pizza\n- Salsa de tomate\n- Queso\n- Jamón\n- Piña', '1. Armar pizza.\n2. Hornear 20 minutos.', '01:00:00', 4, true, 'fernando@gmail.com'),
('Avena con Manzana y Canela', UNHEX('89504E470D0A1A0A'), 'Avena caliente con sabor a manzana.', '- Avena\n- Manzana\n- Canela\n- Leche\n- Miel', '1. Cocinar avena con leche.\n2. Agregar manzana y canela.', '00:15:00', 1, true, 'jbeltrano@unal.edu.co'),
('Raviolis de Espinaca y Queso', UNHEX('89504E470D0A1A0A'), 'Pasta rellena con espinaca y queso ricotta.', '- Masa para pasta\n- Espinaca\n- Ricotta\n- Salsa de tomate', '1. Preparar relleno.\n2. Cocinar y servir.', '01:10:00', 3, true, 'fernando@gmail.com'),
('Enchiladas Suizas', UNHEX('89504E470D0A1A0A'), 'Enchiladas con salsa cremosa de tomatillo.', '- Tortillas\n- Pollo\n- Tomatillo\n- Crema\n- Queso', '1. Preparar salsa.\n2. Rellenar y hornear.\n3. Servir caliente.', '00:50:00', 4, true, 'jbeltrano@unal.edu.co'),
('Risotto de Espinaca', UNHEX('89504E470D0A1A0A'), 'Risotto verde con espinaca y parmesano.', '- Arroz arborio\n- Espinaca\n- Caldo\n- Queso parmesano', '1. Cocinar arroz.\n2. Incorporar espinaca y caldo.\n3. Servir.', '01:00:00', 3, true, 'fernando@gmail.com'),
('Tacos de Carne Asada', UNHEX('89504E470D0A1A0A'), 'Tacos mexicanos con carne a la parrilla.', '- Carne asada\n- Tortillas\n- Cebolla\n- Cilantro\n- Limón', '1. Asar carne.\n2. Servir en tortillas.\n3. Agregar guarniciones.', '00:35:00', 4, true, 'jbeltrano@unal.edu.co'),
('Lasaña de Pollo y Espinaca', UNHEX('89504E470D0A1A0A'), 'Lasaña cremosa con pollo y verduras.', '- Láminas de pasta\n- Pollo\n- Espinaca\n- Salsa bechamel', '1. Preparar relleno.\n2. Armar y hornear 40 minutos.', '01:25:00', 6, true, 'fernando@gmail.com'),
('Tostadas con Hummus', UNHEX('89504E470D0A1A0A'), 'Snack saludable con pan integral y hummus.', '- Pan integral\n- Hummus\n- Tomate\n- Aceite de oliva', '1. Tostar pan.\n2. Untar hummus.\n3. Añadir toppings.', '00:10:00', 2, true, 'jbeltrano@unal.edu.co'),
('Pasta al Pomodoro', UNHEX('89504E470D0A1A0A'), 'Pasta italiana con salsa de tomate casera.', '- Pasta\n- Tomate\n- Ajo\n- Albahaca\n- Aceite de oliva', '1. Cocinar pasta.\n2. Preparar salsa.\n3. Mezclar y servir.', '00:30:00', 3, true, 'fernando@gmail.com'),
('Tamales de Frijol', UNHEX('89504E470D0A1A0A'), 'Tamales vegetarianos con relleno de frijol.', '- Masa de maíz\n- Frijoles refritos\n- Hojas de maíz\n- Salsa', '1. Rellenar hojas.\n2. Cocer al vapor.\n3. Servir.', '01:50:00', 6, true, 'jbeltrano@unal.edu.co'),
('Spaghetti con Albóndigas', UNHEX('89504E470D0A1A0A'), 'Pasta italiana con albóndigas en salsa roja.', '- Spaghetti\n- Albóndigas\n- Salsa de tomate\n- Queso parmesano', '1. Cocinar pasta.\n2. Preparar albóndigas.\n3. Servir juntos.', '01:10:00', 4, true, 'fernando@gmail.com'),
('Sopa de Verduras', UNHEX('89504E470D0A1A0A'), 'Sopa casera saludable con verduras mixtas.', '- Zanahoria\n- Papa\n- Calabaza\n- Caldo vegetal', '1. Cocinar las verduras.\n2. Añadir caldo.\n3. Servir caliente.', '00:40:00', 4, true, 'jbeltrano@unal.edu.co'),
('Pasta con Espárragos y Limón', UNHEX('89504E470D0A1A0A'), 'Pasta ligera con espárragos y limón.', '- Pasta\n- Espárragos\n- Limón\n- Queso parmesano', '1. Cocinar pasta.\n2. Saltear espárragos.\n3. Servir con limón y queso.', '00:35:00', 2, true, 'fernando@gmail.com'),
('Tacos de Verduras Asadas', UNHEX('89504E470D0A1A0A'), 'Tacos vegetarianos con verduras al grill.', '- Tortillas\n- Pimientos\n- Calabacín\n- Cebolla\n- Salsa', '1. Asar verduras.\n2. Servir en tortillas.', '00:25:00', 3, true, 'jbeltrano@unal.edu.co'),
('Ñoquis con Salsa de Tomate', UNHEX('89504E470D0A1A0A'), 'Ñoquis suaves con salsa casera.', '- Ñoquis\n- Tomate\n- Ajo\n- Aceite de oliva\n- Albahaca', '1. Cocinar ñoquis.\n2. Preparar salsa.\n3. Mezclar y servir.', '00:40:00', 3, true, 'fernando@gmail.com'),
('Pan de Avena', UNHEX('89504E470D0A1A0A'), 'Pan casero saludable con avena y miel.', '- Harina integral\n- Avena\n- Levadura\n- Agua\n- Miel', '1. Amasar masa.\n2. Dejar reposar.\n3. Hornear.', '01:30:00', 8, true, 'jbeltrano@unal.edu.co'),
('Pasta con Brócoli y Ajo', UNHEX('89504E470D0A1A0A'), 'Pasta simple y deliciosa con brócoli al ajo.', '- Pasta\n- Brócoli\n- Ajo\n- Aceite de oliva\n- Queso parmesano', '1. Cocinar pasta y brócoli.\n2. Saltear ajo.\n3. Mezclar y servir.', '00:30:00', 3, true, 'fernando@gmail.com');

-- Categorías asociadas
INSERT INTO receta_categoria (receta_id, categoria_id) VALUES
(81, 2),
(82, 4), (82, 5),
(83, 1), (83, 6),
(84, 4), (84, 5),
(85, 1), (85, 6),
(86, 4), (86, 7),
(87, 2),
(88, 4), (88, 7),
(89, 2),
(90, 4), (90, 6),
(91, 6), (91, 7),
(92, 4),
(93, 2), (93, 7),
(94, 4), (94, 5),
(95, 6),
(96, 4), (96, 7),
(97, 2), (97, 7),
(98, 4),
(99, 3), (99, 6),
(100, 4), (100, 6);
