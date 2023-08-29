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
DROP TABLE IF EXISTS spaces_bookings CASCADE;
DROP SEQUENCE IF EXISTS spaces_bookings_id_seq;

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
  booking_date date,
  confirmed boolean,
  booked_by int,
  space_id int
);

CREATE SEQUENCE IF NOT EXISTS spaces_bookings_id_seq;
CREATE TABLE spaces_bookings (
  space_id int,
  booking_id int,
  constraint fk_space foreign key(space_id) references spaces(id) on delete cascade,
  constraint fk_booking foreign key(booking_id) references bookings(id) on delete cascade,
  PRIMARY KEY (space_id, booking_id)
);



-- Finally, we add any records that are needed for the tests to run

INSERT INTO users (email, password) VALUES ('user_1@makers.com', '123453455555!');
INSERT INTO users (email, password) VALUES ('user_2@makers.com', '678944676787@');
INSERT INTO users (email, password) VALUES ('user_3@makers.com', 'abcdef222222$');

INSERT INTO spaces (name, description, price, avail_from, avail_to, user_id) VALUES ('House_1', 'nice house', 150.00, '01/01/2023', '01/10/2023', 1);
INSERT INTO spaces (name, description, price, avail_from, avail_to, user_id) VALUES ('House_2', 'nice pool', 250.00, '01/04/2023', '01/09/2023', 2);
INSERT INTO spaces (name, description, price, avail_from, avail_to, user_id) VALUES ('House_3', 'nice garden', 350.00, '01/06/2023', '01/11/2023', 3);

INSERT INTO bookings (booking_date, confirmed, booked_by, space_id) VALUES ('2023/7/10', True, 3, 1);
INSERT INTO bookings (booking_date, confirmed, booked_by, space_id) VALUES ('2023/8/15', True, 2, 2);
INSERT INTO bookings (booking_date, confirmed, booked_by, space_id) VALUES ('2023/9/20', True, 1, 3);

INSERT INTO spaces_bookings (space_id, booking_id) VALUES (1, 3);
INSERT INTO spaces_bookings (space_id, booking_id) VALUES (2, 2);
INSERT INTO spaces_bookings (space_id, booking_id) VALUES (3, 1);






