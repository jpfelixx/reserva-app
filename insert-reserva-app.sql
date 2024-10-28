/* inserts */
use reserva_app;

INSERT INTO Usuario (nome, email, password, admin) VALUES
('João Pedro', 'joaomontlix@gmail.com', 'mari1234', False),
('Jossana Tavares', 'jojotavares@gmail.com', '555Sainz', False),
('Marisa Mayumi', 'marismayu@gmail.com', 'EuAmoPop', False),
('Millena Cupolillo', 'millenacup@gmail.com', 'mihCopoo', False),
('Professor Latorre', 'latorre@gmail.com', 'Latorre1', False);


INSERT INTO Sala (tipo, capacidade, descricao, ativa) VALUES
('Sala de Aula', 22, 'aula de biologia', True),
('Laboratório de Informática', 4, 'aula de python', False),
('Sala de Aula', 12, 'aula de literatura', True),
('Sala de Aula', 10, 'aula de literatura', True),
('Sala de Aula', 20, 'matsumoto', True);

INSERT INTO Reserva (fk_Sala_idSala, fk_Usuario_idUsuario, inicio, fim) VALUES
(5, 1, '2024-10-25 11:06:00', '2024-08-01 16:06:00'),
(3, 4, '2024-10-22 12:16:00', '2024-07-25 16:16:00'),
(1, 3, '2024-10-26 16:20:00', '2024-07-27 20:20:00'),
(2, 5, '2024-07-25 16:06:00', '2024-08-01 16:06:00'),
(1, 5, '2024-07-22 16:16:00', '2024-07-25 16:16:00'),
(4, 5, '2024-07-26 16:20:00', '2024-07-27 16:20:00');


