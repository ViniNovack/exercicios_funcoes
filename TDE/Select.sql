-- ---------------- CONFERENCIA ----------------
-- O resultado desta consulta deve ser: 14 6 7 8 24
SELECT (SELECT COUNT(*) FROM aluno) AS alunos,
(SELECT COUNT(*) FROM professor) AS professores,
(SELECT COUNT(*) FROM curso) AS cursos,
(SELECT COUNT(*) FROM turma) AS turmas,
(SELECT COUNT(*) FROM matricula) AS matriculas;

-- ___________________________PARTE 2___________________________
-- Liste o nome e a cidade de todos os alunos, em ordem alfabética de nome
select nome, cidade from aluno
order by nome asc;

-- Liste o nome dos cursos com carga horária maior que 40 horas
select nome_curso from curso
where carga_horaria > 40
order by nome_curso asc;

-- Mostre apenas o número total de alunos nascidos depois do ano de 2005
select count(id) from aluno
where data_nascimento > 2005;

-- Exiba nome, matrícula e idade (em anos) de cada aluno, do mais velho para o mais novo
select nome, matricula, TIMESTAMPDIFF(YEAR, data_nascimento, CURDATE()) from aluno
ORDER BY data_nascimento ASC;

-- Mostre todas as turmas com o nome do curso e o nome do professor responsável
select t.nome_turma, c.nome_curso, p.nome from turma as t
join curso as c on t.id_curso = c.id
join professor as p on t.id_professor = p.id
order by t.nome_turma;

-- Liste os alunos matriculados em turmas do curso de "Matemática"
select a.nome from aluno as a
join matricula as m on a.id = m.id_turma
join turma as t on m.id_turma = t.id
join curso as c on t.id_curso = c.id
where c.nome_curso like "Matemática";

-- Mostre, para cada curso, quantos alunos estão matriculados em suas turmas. Ordene do maior para o menor
select c.nome_curso, count(m.id) as matriculados from curso as c
join turma as t on c.id = t.id_curso
join matricula as m on t.id = m.id_turma
group by c.id, c.nome_curso
order by matriculados desc;

-- Exiba, para cada cidade, quantos alunos residem nela. Ordene do maior para o menor
-- Mostre o nome dos alunos que NÃO possuem nenhuma matrícula com status "Ativa"
-- Liste o nome dos cursos que não possuem nenhuma turma cadastrada
-- Liste os professores que ministram mais de uma turma, mostrando o nome e a quantidade de turmas
-- [DESAFIO] Liste os alunos que possuem matrícula ativa simultaneamente em turmas de "Biologia" e de "Matemática".