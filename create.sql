PRAGMA foreign_keys = off;

.headers on
.mode columns

DROP TABLE IF EXISTS Problem;
DROP TABLE IF EXISTS Theme;
DROP TABLE IF EXISTS ProblemTheme;

CREATE TABLE Problem (
    id          INTEGER
                PRIMARY KEY
                AUTOINCREMENT,

    location    TEXT
                NOT NULL
                UNIQUE
);

CREATE TABLE Theme (
    id          INTEGER
                PRIMARY KEY
                AUTOINCREMENT,

    name        TEXT
                NOT NULL
                UNIQUE
);

CREATE TABLE ProblemTheme (
    problemId   INTEGER
                REFERENCES Problem ON UPDATE CASCADE ON DELETE CASCADE,

    themeId     INTEGER
                REFERENCES Theme ON UPDATE CASCADE ON DELETE CASCADE,

    PRIMARY KEY(problemId, themeId)
);