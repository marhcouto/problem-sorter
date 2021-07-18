PRAGMA foreign_keys = on;

INSERT INTO Problem (location) VALUES ("has");
INSERT INTO Problem (location) VALUES ("asd");
INSERT INTO Problem (location) VALUES ("asdas");
INSERT INTO Problem (location) VALUES ("fs");
INSERT INTO Problem (location) VALUES ("asfa asd");
INSERT INTO Problem (location) VALUES ("fasfh 5r  t");

INSERT INTO Theme (name) VALUES ("theme 1");
INSERT INTO Theme (name) VALUES ("theme 2");
INSERT INTO Theme (name) VALUES ("theme 3");
INSERT INTO Theme (name) VALUES ("theme 4");
INSERT INTO Theme (name) VALUES ("theme 5");

INSERT INTO ProblemTheme(problemId, themeId) VALUES (1, 2);
INSERT INTO ProblemTheme(problemId, themeId) VALUES (1, 3);
INSERT INTO ProblemTheme(problemId, themeId) VALUES (1, 4);
INSERT INTO ProblemTheme(problemId, themeId) VALUES (2, 1);
INSERT INTO ProblemTheme(problemId, themeId) VALUES (3, 1);
INSERT INTO ProblemTheme(problemId, themeId) VALUES (4, 5);