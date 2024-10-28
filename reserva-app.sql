/* Lógico_1: */
create database reserva_app;

use reserva_app;

CREATE TABLE Usuario (
    idUsuario integer auto_increment PRIMARY KEY,
    nome varchar (50),
    email varchar (50),
    password char (8),
    admin boolean
);

CREATE TABLE Sala (
    idSala integer auto_increment PRIMARY KEY,
    tipo varchar (50),
    capacidade integer,
    descricao varchar (100),
    ativa boolean
);

CREATE TABLE Reserva (
	idReserva integer auto_increment PRIMARY KEY,
    fk_Sala_idSala integer,
    fk_Usuario_idUsuario integer,
    inicio datetime,
    fim datetime
);

ALTER TABLE Reserva ADD CONSTRAINT FK_Reserva_2
    FOREIGN KEY (fk_Sala_idSala)
    REFERENCES Sala (idSala)
    ON DELETE SET NULL;

ALTER TABLE Reserva ADD CONSTRAINT FK_Reserva_3
    FOREIGN KEY (fk_Usuario_idUsuario)
    REFERENCES Usuario (idUsuario)
    ON DELETE SET NULL;
