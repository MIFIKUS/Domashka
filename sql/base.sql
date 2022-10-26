CREATE TABLE users(
    id INTEGER NOT NULL PRIMARY KEY,
    login VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE students(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL
);

INSERT INTO users(login, password)
VALUES ('login', 'password'), ('login1', 'password1');

INSERT INTO students(name, surname)
VALUES ('name', 'surname'), ('name1', 'surname1');