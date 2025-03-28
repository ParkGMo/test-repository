import React from "react";
// import Back from "./categories/Back";
// import Chest from "./categories/Chest";
// import Arms from "./categories/Arms";
// import Abs from "./categories/Abs";
// import Cardio from "./categories/Cardio";
import styles from "./FitnessCategories.module.scss";
import LowerBody from "./LowerBody/LowerBody";

const FitnessCategories = () => {
  return (
    <div className={styles.container}>
      <h1>운동 카테고리</h1>
      <div className={styles.categories}>
        <LowerBody />
        {/* <Back />
        <Chest />
        <Arms />
        <Abs />
        <Cardio /> */}
      </div>
    </div>
  );
};

export default FitnessCategories;
