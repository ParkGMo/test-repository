CREATE TABLE Workout (
    workout_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    workout_date DATE NOT NULL,
    workout_type VARCHAR(50) NOT NULL,  -- 예: '웨이트', '러닝', '요가'
    duration_minutes INT, -- 운동 지속 시간(분)
    -- calories_burned DECIMAL(6,2),
    notes TEXT, -- 사용자 운동 메모
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE
);