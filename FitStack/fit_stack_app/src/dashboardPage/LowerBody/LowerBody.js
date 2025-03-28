import React, { useState } from "react";
import styles from "./LowerBody.module.scss";

const lowerBodyExercises = [
  { id: 1, name: "스쿼트" },
  { id: 2, name: "브이스쿼트" },
  { id: 3, name: "데드리프트" },
  { id: 4, name: "레그 프레스" },
  { id: 5, name: "런지" },
];

const LowerBody = ({ onSelectExercise }) => {
  const [selectedExercises, setSelectedExercises] = useState([]);

  const handleSelect = (exercise) => {
    if (!selectedExercises.includes(exercise)) {
      const updatedList = [...selectedExercises, exercise];
      setSelectedExercises(updatedList);
      onSelectExercise(updatedList); // 부모 컴포넌트로 선택한 운동 전달
    }
  };

  return (
    <div className={styles.lowerBodyContainer}>
      <h2>하체 운동 선택</h2>
      <div className={styles.exerciseList}>
        {lowerBodyExercises.map((exercise) => (
          <div
            key={exercise.id}
            className={styles.exerciseCard}
            onClick={() => handleSelect(exercise)}
          >
            <div className={styles.imagePlaceholder}>
              {/* 여기에 이미지 추가 예정 */}
            </div>
            <p>{exercise.name}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default LowerBody;
