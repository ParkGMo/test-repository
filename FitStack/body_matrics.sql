CREATE TABLE Body_Metrics (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    record_date DATE NOT NULL,
    weight_kg DECIMAL(5,2) NOT NULL,
    body_fat_percentage DECIMAL(5,2),
    muscle_mass_kg DECIMAL(5,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE
);
