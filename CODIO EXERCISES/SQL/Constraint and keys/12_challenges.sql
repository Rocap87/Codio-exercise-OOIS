USE blog;

SELECT posts.user_id, users.name, posts.body 
FROM posts
RIGHT OUTER JOIN users ON 
posts.user_id = users.id;

USE blog;

CREATE TABLE comments (
  id INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  body TEXT DEFAULT NULL,
  user_id INT(7) UNSIGNED NOT NULL,
  PRIMARY KEY (id)) AUTO_INCREMENT = 1;

USE blog;

ALTER TABLE comments
ADD COLUMN post_id INT(3) UNSIGNED NOT NULL
ADD CONSTRAINT FOREIGN KEY (post_id)
REFERENCES posts(id);