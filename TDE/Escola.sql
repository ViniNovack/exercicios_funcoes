-- ============================================================
-- BANCO DE DADOS "escola" - script completo de criacao
-- Execute este script inteiro no MySQL Workbench antes da Parte 2
-- ============================================================
DROP DATABASE IF EXISTS escola;
CREATE DATABASE escola CHARACTER SET utf8mb4;
USE escola;

CREATE TABLE aluno (
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(80) NOT NULL,
matricula VARCHAR(15) NOT NULL UNIQUE,
data_nascimento DATE NOT NULL,
cidade VARCHAR(50) NOT NULL
);

CREATE TABLE professor (
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(80) NOT NULL,
especialidade VARCHAR(60) NOT NULL
);

CREATE TABLE curso (
id INT PRIMARY KEY AUTO_INCREMENT,
nome_curso VARCHAR(60) NOT NULL,
carga_horaria INT NOT NULL
);

-- Guardar em qual sala e em qual horário cada turma acontece  (INFRAESTRUTURA)
CREATE TABLE infraestrutura(
	id int not null auto_increment,
    sala int not null,
    hora_inicio time not null,
    hora_fim time not null,
    primary key(id)
);

CREATE TABLE turma (
id INT PRIMARY KEY AUTO_INCREMENT,
nome_turma VARCHAR(30) NOT NULL,
id_curso INT NOT NULL,
id_professor INT NOT NULL,
vagas INT NOT NULL DEFAULT 30,
FOREIGN KEY (id_curso) REFERENCES curso(id),
FOREIGN KEY (id_professor) REFERENCES professor(id),

-- infraestrutura
id_infraestrutura int null,
foreign key (id_infraestrutura) references infraestrutura(id)
);

CREATE TABLE matricula (
id INT PRIMARY KEY AUTO_INCREMENT,
id_aluno INT NOT NULL,
id_turma INT NOT NULL,
data_matricula DATE NOT NULL,
status ENUM('Ativa','Trancada','Cancelada') NOT NULL,
FOREIGN KEY (id_aluno) REFERENCES aluno(id),
FOREIGN KEY (id_turma) REFERENCES turma(id)
);

-- Registrar as notas de cada aluno em cada turma, por avaliação (prova, trabalho, recuperação)  (notas)
CREATE TABLE notas(
	id int not null auto_increment,
    id_matricula int not null,
    avaliacao varchar(45) not null,
    tipo enum('prova', 'trabalho', 'recuperacao') not null,
    valor decimal(4,2) not null,
    primary key(id),
    foreign key (id_matricula) references matricula(id)
);

-- Controlar a frequência: presença ou falta do aluno em cada aula  (frequencia)
CREATE TABLE frequencia(
	id int not null auto_increment,
    id_matricula int not null,
    aula int not null,
    dia date,
    presenca enum('presente', 'falta') not null,
    primary key(id),
    foreign key (id_matricula) references matricula(id)
);