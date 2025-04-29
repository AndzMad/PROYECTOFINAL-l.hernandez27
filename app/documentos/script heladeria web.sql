CREATE DATABASE heladeria_web;
USE heladeria_web;

SELECT * FROM usuario;
drop table usuario;

CREATE TABLE ingredientes(
id int primary key,
tipo varchar(50),
nombre varchar(50),
precio float,
calorias int,
inventario float,
vegetariano bool,
sabor varchar(50) null);

CREATE TABLE productos(
id int primary key,
tipo varchar(50),
nombre varchar(50),
id_ingrediente1 int,
id_ingrediente2 int,
id_ingrediente3 int,
precio_publico float,
volumen int null,
tipo_vaso varchar(15) null,
foreign key (id_ingrediente1) references ingredientes(id),
foreign key (id_ingrediente2) references ingredientes(id),
foreign key (id_ingrediente3) references ingredientes(id)  );

INSERT INTO ingredientes (id, tipo, nombre, precio, calorias, inventario, vegetariano, sabor) 
VALUES
(1, 'Base', 'Helado de Fresa', 1200, 150, 10, TRUE, 'Fresa'),
(2, 'Base', 'Helado de Vainilla', 1100, 140, 8, TRUE, 'Vainilla'),
(3, 'Base', 'Helado de Chocolate', 1300, 160, 12, TRUE, 'Chocolate'),
(4, 'Base', 'Helado de Menta', 1250, 135, 9, TRUE, 'Menta');

INSERT INTO ingredientes (id, tipo, nombre, precio, calorias, inventario, vegetariano, sabor) 
VALUES
(5, 'Complemento', 'Chispas de Chocolate', 500, 80, 5, TRUE, NULL),
(6, 'Complemento', 'Maní Japonés', 900, 200, 3, FALSE, NULL),
(7, 'Complemento', 'Sirope de Caramelo', 700, 120, 7, TRUE, NULL),
(8, 'Complemento', 'Galletas Trituradas', 600, 90, 4, TRUE, NULL),
(9, 'Complemento', 'Nueces Caramelizadas', 950, 180, 6, FALSE, NULL),
(10, 'Complemento', 'Coco Rallado', 550, 70, 6, TRUE, NULL),
(11, 'Complemento', 'Frutas Confitadas', 800, 150, 5, TRUE, NULL),
(12, 'Complemento', 'Mermelada de Fresa', 750, 130, 7, TRUE, NULL);

SELECT * FROM ingredientes;

INSERT INTO productos (id, tipo, nombre, id_ingrediente1, id_ingrediente2, id_ingrediente3, precio_publico, volumen, tipo_vaso) 
VALUES
(1, 'Copa', 'Copa Samurai de Fresas', 1, 12, 6, 7500, NULL, 'Vaso de vidrio'),
(2, 'Copa', 'Copa Elegancia Vainilla', 2, 8, 6, 7200, NULL, 'Vaso cerámico'),
(3, 'Malteada', 'Malteada Chocoespacial', 2, 5, 9, 9000, 16, NULL),
(4, 'Malteada', 'Malteada Dulce Fresa', 1, 11, 7, 8500, 16, NULL);
