CREATE TABLE Person (
    personId INT,
    lastName VARCHAR,
    firstName VARCHAR
);

CREATE TABLE Address (
    addressId INT,
    personId INT,
    city VARCHAR,
    state VARCHAR
);

INSERT INTO Person VALUES (1, 'Wang', 'Allen');
INSERT INTO Person VALUES (2, 'Alice', 'Bob');
INSERT INTO Address VALUES (1, 2, 'New York City', 'New York');
INSERT INTO Address VALUES (2, 3, 'Leetcode', 'California');
