-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables

DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;

-- Then, we recreate them

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255)
);

-- Maybe phone number, to receive a text message after booking

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name text,
  description text,
  price float,
  avail_from date,
  avail_to date,
  profile_photo text,
  user_id int,
  constraint fk_user_id foreign key(user_id) references users(id) on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  booking_date date,
  booked_by int,
  space_id int,
  constraint fk_booked_by foreign key(booked_by) references users(id) on delete cascade,
  constraint fk_space_id foreign key(space_id) references spaces(id) on delete cascade
);

-- Maybe booking total price?!

-- Finally, we add any records that are needed for the tests to run

INSERT INTO users (email, password) VALUES ('user_1@makers.com', '123453455555!');
INSERT INTO users (email, password) VALUES ('user_2@makers.com', '678944676787@');
INSERT INTO users (email, password) VALUES ('user_3@makers.com', 'abcdef222222$');

INSERT INTO spaces (name, description, price, avail_from, avail_to, profile_photo, user_id) VALUES ('House_1', 'nice house', 150.00, '2023/01/01', '2023/10/01', 'https://images.unsplash.com/photo-1554995207-c18c203602cb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8aG91c2V8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=800&q=60', 1);
INSERT INTO spaces (name, description, price, avail_from, avail_to, profile_photo, user_id) VALUES ('House_2', 'nice pool', 250.00, '2023/04/01', '2023/09/01','https://images.unsplash.com/photo-1564013799919-ab600027ffc6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGhvdXNlfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60', 2);
INSERT INTO spaces (name, description, price, avail_from, avail_to, profile_photo, user_id) VALUES ('House_3', 'nice garden', 350.00, '2023/06/01', '2023/11/01','https://images.unsplash.com/photo-1568605114967-8130f3a36994?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8aG91c2V8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=800&q=60', 3);


INSERT INTO bookings (booking_date, booked_by, space_id) VALUES ('2023/7/10', 3, 1);
INSERT INTO bookings (booking_date, booked_by, space_id) VALUES ('2023/8/15', 2, 2);
INSERT INTO bookings (booking_date, booked_by, space_id) VALUES ('2023/9/20', 1, 3);
