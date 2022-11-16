CREATE TABLE post(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(100)  NOT NULL
);

CREATE TABLE users(
    id INTEGER NOT NULL PRIMARY KEY,
    login VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    post INTEGER NOT NULL,
    FOREIGN KEY (post) REFERENCES post(id)
);

CREATE TABLE students(
    id INTEGER NOT NULL PRIMARY KEY,
    surname VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE subjects(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(150)
);

CREATE TABLE marks(
    id INTEGER NOT NULL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    mark INTEGER NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id)
                  ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
                  ON DELETE CASCADE ON UPDATE NO ACTION
);

INSERT INTO post(id, name) VALUES (1, 'Admin'), (2, "Director");
INSERT INTO users(id, login, password, post) VALUES (1, 'admin', 'admin', 1);