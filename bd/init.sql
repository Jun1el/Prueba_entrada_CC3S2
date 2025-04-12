DROP TABLE IF EXISTS questions;

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    options TEXT[] NOT NULL,
    correct_answer INTEGER NOT NULL,
    difficulty TEXT NOT NULL
);

INSERT INTO questions (description, options, correct_answer, difficulty) VALUES
('¿Cuál es la capital de Perú?', ARRAY['Lima', 'Cusco', 'Arequipa'], 0, 'Fácil'),
('¿Cuánto es 2 + 2?', ARRAY['3', '4', '5'], 1, 'Fácil'),
('¿Quién escribió Don Quijote?', ARRAY['Miguel de Cervantes', 'Pablo Neruda', 'Gabriel García Márquez'], 0, 'Media'),
('¿Cuál es el planeta más grande del sistema solar?', ARRAY['Tierra', 'Marte', 'Júpiter'], 2, 'Media'),
('¿En qué continente está Egipto?', ARRAY['Asia', 'África', 'Europa'], 1, 'Fácil'),
('¿Cuál es el resultado de 9 * 6?', ARRAY['54', '56', '64'], 0, 'Media'),
('¿Qué gas respiramos para vivir?', ARRAY['Oxígeno', 'Dióxido de carbono', 'Nitrógeno'], 0, 'Fácil'),
('¿Cuántos lados tiene un hexágono?', ARRAY['5', '6', '8'], 1, 'Media'),
('¿En qué año terminó la Segunda Guerra Mundial?', ARRAY['1945', '1939', '1950'], 0, 'Difícil'),
('¿Quién pintó la Mona Lisa?', ARRAY['Leonardo da Vinci', 'Picasso', 'Van Gogh'], 0, 'Media');
