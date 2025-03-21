import React, { useState } from "react";
import axios from "axios";
// import "./Login.scss"; // SCSS 파일 import
import styles from "./Login.module.scss";

const Login = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/login", {
        username,
        email,
        password,
      });

      setMessage("로그인 성공!");
      localStorage.setItem("token", response.data.token);
    } catch (error) {
      setMessage(
        "로그인 실패: " + (error.response?.data?.message || "서버 오류")
      );
    }
  };

  return (
    <div className={styles.login_container}>
      <h1>
        <span className={styles.fit}>FIT</span>
        <span className={styles.track}>Track</span>
      </h1>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="닉네임"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type="email"
          placeholder="이메일"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="비밀번호"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">로그인</button>
      </form>
      {message && <p className={styles.message}>{message}</p>}
      <div className={styles.links}>
        <a href="/forgot-password">비밀번호 찾기</a>
        <a href="/register">회원가입</a>
      </div>
    </div>
  );
};

export default Login;
