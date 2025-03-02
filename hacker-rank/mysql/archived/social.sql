CREATE TABLE users (

  user_id INT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

CREATE TABLE posts (

  post_id INT PRIMARY KEY,
  user_id INT,
  content TEXT,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE comments (

  comment_id INT PRIMARY KEY,
  user_id INT,
  content TEXT,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, username, email) VALUES
(1, 'john_doe', 'john.doe@example.com'),
(2, 'jane_doe', 'jane.doe@example.com'),
(3, 'peter_pan', 'peter.pan@example.com');

INSERT INTO posts (post_id, user_id, content) VALUES
(1, 1, 'First post'),
(2, 2, 'Second post'),
(3, 3, 'Third post');

INSERT INTO comments (comment_id, user_id, content) VALUES
(1, 1, 'First comment'),
(2, 2, 'Second comment'),
(3, 3, 'Third comment');