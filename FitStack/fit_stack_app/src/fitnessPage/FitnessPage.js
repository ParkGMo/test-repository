import React, { useState } from "react";
import styles from "./FitnessPage.module.scss";
import LowerBody from "../dashboardPage/LowerBody/LowerBody";
import WorkOutList from "./workOutListPage/WorkOutListPage";

const FitnessPage = () => {
  const [selectedExercises, setSelectedExercises] = useState([]);

  return (
    <div className={styles.fitnessPageContainer}>
      <LowerBody onSelectExercise={setSelectedExercises} />
      <WorkOutList selectedExercises={selectedExercises} />
    </div>
  );
};

export default FitnessPage;
