import React, { useState } from "react";
import axios from "axios";
import styles from "./Register.module.scss";

const now = Date.now();

const Register = () => {
  const [formData, setFormData] = useState({
    userid: 3,
    username: "",
    email: "",
    password: "",
    age: "",
    gender: "Male",
    height_cm: "",
    weight_kg: "",
    created_at: now,
    updated_at: now,
    deleted_at: now,
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:5000/api/register",
        formData
      );
      alert("회원가입 성공!");
    } catch (error) {
      console.error("회원가입 실패:", error);
      alert("회원가입 중 오류가 발생했습니다.");
    }
  };

  return (
    <div className={styles.userForm}>
      <h2>회원가입</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="닉네임"
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="이메일"
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="비밀번호"
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="age"
          placeholder="나이"
          onChange={handleChange}
        />

        <select name="gender" onChange={handleChange}>
          <option value="Male">남성</option>
          <option value="Female">여성</option>
          <option value="Other">기타</option>
        </select>

        <input
          type="number"
          name="height_cm"
          placeholder="키 (cm)"
          step="0.1"
          onChange={handleChange}
        />
        <input
          type="number"
          name="weight_kg"
          placeholder="몸무게 (kg)"
          step="0.1"
          onChange={handleChange}
        />

        <button type="submit">가입하기</button>
      </form>
    </div>
  );
};

export default Register;
