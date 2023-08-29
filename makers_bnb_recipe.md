# Two Tables (Many-to-Many) Design Recipe Template

_Copy this recipe template to design and create two related database tables having a Many-to-Many relationship._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORIES:

As a user I can sign-up or log-in, with an email and password.

As a user I can see the list of spaces that are available to rent (or, no spaces if none have been created) with descriptions and price per night.

As a User I can see multiple spaces.

As a user I can request to hire any space for one night. Until a user has confirmed a booking request, that space can still be booked for that night.

As a user I can approve another user's request to hire a space for one night

```

```
Nouns:

User, spaces, email, password, night, booking, request, price, requests, description.
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record   | Properties                                                                    |
| -------- | ----------------------------------------------------------------------------- |
| Users    | email, password                                                               |
| Spaces   | name, decription, ppn, avail from, avail to, booking_date, confirmed, user_id |
| Bookings | space_id, user_id                                                             |

1. Name of the first table (always plural): `users`

   Column names: `email`, `password`

2. Name of the second table (always plural): `Spaces`

   Column names: `name`, `decription`, `ppn`, `avail from`, `avail to`, `booking_date`, `confirmed`,`user_id`

3. Name of the join table (always plural): `bookings`

   Column names: `space_id`, `user_id`

## 3. Decide the column types.

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: users
id: SERIAL
email: text
password: text


Table: spaces
id: SERIAL
name: text
description: text
price: float
avail from: date
avail to: date
booking_date: date
confirmed: text
user_id: int

```

## 4. Design the Many-to-Many relationship

```
# EXAMPLE

1. Can one user have many spaces? YES
2. Can one space have many users? YES
```

## 5. Design the Join Table

The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is `table1_table2`.

```
# EXAMPLE

Join table for tables: items and orders
Join table name: items_orders
Columns: item_id, order_id
```

## 4. Write the SQL.

```sql
-- Create the first table.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name text,
  password text,
);

-- Create the second table.
CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name text,
  description text,
  price float,
  avail_from date,
  avail_to date,
  booking_date date,
  comfirmed boolean,
  booked_by, int,
  user_id, int
);

-- Create the join table.
CREATE TABLE bookings (
  space_id int,
  booked_by int,
  constraint fk_spaces foreign key(space_id) references spaces(id) on delete cascade,
  constraint fk_user foreign key(booked_by) references users(id) on delete cascade,
  PRIMARY KEY (space_id, booked_by)
);

```

## 5. Create the tables.

```bash
psql -h 127.0.0.1 shop_manager_project < shop_items_orders.sql
```
