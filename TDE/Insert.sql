-- ---------------- PROFESSORES ----------------
INSERT INTO professor (nome, especialidade) VALUES
('Ana Ribeiro', 'Ciências Exatas'),
('Bruno Carvalho', 'Ciências Exatas'),
('Carla Menezes', 'Ciências Biológicas'),
('Diego Almeida', 'Linguagens'),
('Elisa Tavares', 'Ciências Humanas'),
('Fábio Nunes', 'Ciências Exatas');
-- ---------------- CURSOS ----------------
INSERT INTO curso (nome_curso, carga_horaria) VALUES
('Matemática', 60),
('Física', 45),
('Biologia', 40),
('Química', 50),
('História', 30),
('Português', 80),
('Educação Física', 20);
-- ---------------- TURMAS ----------------
INSERT INTO turma (nome_turma, id_curso, id_professor, vagas) VALUES
('MAT-1A', 1, 1, 30),
('MAT-2B', 1, 2, 25),
('FIS-1A', 2, 1, 20),
('BIO-1A', 3, 3, 28),
('BIO-2C', 3, 3, 22),
('HIS-1A', 5, 5, 35),
('POR-1A', 6, 4, 30),
('POR-2B', 6, 4, 30);
-- ---------------- ALUNOS ----------------
INSERT INTO aluno (nome, matricula, data_nascimento, cidade) VALUES
('Alice Moreira', '2026001', '2004-03-12', 'Curitiba'),
('Bernardo Lima', '2026002', '2006-07-25', 'Curitiba'),
('Camila Souza', '2026003', '2005-11-02', 'São José dos Pinhais'),
('Daniel Rocha', '2026004', '2007-01-18', 'Pinhais'),
('Eduarda Pires', '2026005', '2003-09-30', 'Curitiba'),
('Felipe Andrade', '2026006', '2006-02-14', 'Colombo'),
('Gabriela Nunes', '2026007', '2008-05-06', 'São José dos Pinhais'),
('Henrique Barros', '2026008', '2004-12-21', 'Curitiba'),
('Isabela Cardoso', '2026009', '2007-08-09', 'Pinhais'),
('João Vitor Melo', '2026010', '2005-04-27', 'São José dos Pinhais'),
('Karina Duarte', '2026011', '2009-06-15', 'Colombo'),
('Lucas Ferreira', '2026012', '2003-02-03', 'Curitiba'),
('Mariana Alves', '2026013', '2006-10-11', 'São José dos Pinhais'),
('Nicolas Prado', '2026014', '2008-03-22', 'Pinhais');
-- ---------------- MATRICULAS ----------------
INSERT INTO matricula (id_aluno, id_turma, data_matricula, status) VALUES
( 1, 1, '2026-02-10', 'Ativa'),
( 1, 4, '2026-02-10', 'Ativa'),
( 1, 7, '2026-02-11', 'Ativa'),
( 2, 1, '2026-02-10', 'Ativa'),
( 2, 4, '2026-02-12', 'Trancada'),
( 3, 2, '2026-02-13', 'Ativa'),
( 3, 5, '2026-02-13', 'Ativa'),
( 4, 4, '2026-02-14', 'Ativa'),
( 4, 6, '2026-02-14', 'Ativa'),
( 5, 1, '2026-02-15', 'Ativa'),
( 5, 2, '2026-02-15', 'Ativa'),
( 6, 3, '2026-02-16', 'Ativa'),
( 6, 7, '2026-02-16', 'Ativa'),
( 7, 5, '2026-02-17', 'Ativa'),
( 7, 8, '2026-02-17', 'Ativa'),
( 8, 3, '2026-02-18', 'Ativa'),
( 9, 6, '2026-02-18', 'Ativa'),
( 9, 8, '2026-02-19', 'Cancelada'),
(10, 2, '2026-02-19', 'Ativa'),
(10, 3, '2026-02-20', 'Trancada'),
(12, 7, '2026-02-20', 'Trancada'),
(13, 1, '2026-02-21', 'Ativa'),
(13, 6, '2026-02-21', 'Ativa'),
(14, 8, '2026-02-22', 'Cancelada');