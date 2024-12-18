-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe_name text,
    cooking_time int,
    rating int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Fried rice', 10, 3);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Butter chicken', 35, 4);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Easy quiche', 45, 5);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Steak and onions', 25, 5);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Lasagne', 75, 4);