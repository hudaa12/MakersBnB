-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

-- Then, we recreate them

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name text,
  description text,
  price float,
  avail_from date,
  avail_to date,
  user_id int
);


CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  space_id int,
  booked_by int,
  booking_date date,
  confirmed boolean,
  booked_by int,
  constraint fk_spaces foreign key(space_id) references spaces(id) on delete cascade,
  constraint fk_user foreign key(booked_by) references users(id) on delete cascade,
  PRIMARY KEY (space_id, booked_by)
);

-- Finally, we add any records that are needed for the tests to run

INSERT INTO users (email, password) VALUES ('user_1@makers.com', '123453455555!');
INSERT INTO users (email, password) VALUES ('user_2@makers.com', '678944676787@');
INSERT INTO users (email, password) VALUES ('user_3@makers.com', 'abcdef222222$');

INSERT INTO spaces (name, description, price, avail_from, avail_to, user_id) VALUES ('House_1', 'nice house', 150.00, '01/01/2023', '01/10/2023', 1);
INSERT INTO spaces (name, description, price, avail_from, avail_to, user_id) VALUES ('House_2', 'nice pool', 250.00, '01/04/2023', '01/09/2023', 2);
INSERT INTO spaces (name, description, price, avail_from, avail_to, user_id) VALUES ('House_3', 'nice garden', 350.00, '01/06/2023', '01/11/2023', 3);

INSERT INTO bookings (booking_date, confirmed, booked_by, space_id) VALUES ('10/07/2023', True, 3, 1);
INSERT INTO bookings (booking_date, confirmed, booked_by, space_id) VALUES ('15/08/2023', True, 2, 2);
INSERT INTO bookings (booking_date, confirmed, booked_by, space_id) VALUES ('20/09/2023', True, 1, 3);






