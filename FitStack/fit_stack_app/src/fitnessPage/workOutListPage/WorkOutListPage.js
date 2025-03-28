import React from "react";
import styles from "./WorkOutListPage.module.scss";

const WorkOutList = ({ selectedExercises }) => {
  return (
    <div className={styles.workoutListContainer}>
      <h2>오늘의 운동</h2>
      <ul>
        {selectedExercises.map((exercise, index) => (
          <li key={index}>{exercise.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default WorkOutList;
