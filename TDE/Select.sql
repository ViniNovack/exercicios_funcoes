-- ---------------- CONFERENCIA ----------------
-- O resultado desta consulta deve ser: 14 6 7 8 24
SELECT (SELECT COUNT(*) FROM aluno) AS alunos,
(SELECT COUNT(*) FROM professor) AS professores,
(SELECT COUNT(*) FROM curso) AS cursos,
(SELECT COUNT(*) FROM turma) AS turmas,
(SELECT COUNT(*) FROM matricula) AS matriculas;