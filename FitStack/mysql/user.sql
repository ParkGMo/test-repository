USE fittrack;

DROP TABLE IF EXISTS fit_user;

CREATE TABLE fit_user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    age INT,
    gender ENUM('Male', 'Female', 'Other'),
    height_cm DECIMAL(5,2),
    weight_kg DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO fit_user VALUES (1, '에스파', 'aespa@google.com', 'a123', 30,'Female', 170, 45, '2025-03-20 16:59:00', '2025-03-20 16:59:00', '2025-03-20 16:59:00');
INSERT INTO fit_user VALUES (2, '엔믹스', 'nmixx@google.com', 'n123', 28,'Female', 268, 50, '2025-03-20 16:59:00', '2025-03-20 16:59:00', '2025-03-20 16:59:00');
 