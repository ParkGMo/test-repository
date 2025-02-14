CREATE TABLE Workout_Detail (
    detail_id INT AUTO_INCREMENT PRIMARY KEY,
    workout_id INT NOT NULL,
    exercise_name VARCHAR(100) NOT NULL, -- 예: '벤치프레스', '스쿼트'
    sets INT NOT NULL,
    reps INT NOT NULL,
    weight_kg DECIMAL(5,2), -- 웨이트 운동일 경우
    distance_km DECIMAL(5,2), -- 러닝 등 거리 운동일 경우
    duration_minutes INT, -- 개별 운동 수행 시간
    FOREIGN KEY (workout_id) REFERENCES Workout(workout_id) ON DELETE CASCADE
);
