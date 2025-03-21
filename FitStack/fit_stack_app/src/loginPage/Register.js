import { useState } from "react";
import axios from "axios";
import styles from "./Register.module.scss";

const Register = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://localhost:5000/api/register", {
        username,
        email,
        password,
      });

      if (response.data.success) {
        setMessage("회원가입 성공! 로그인해주세요.");
      } else {
        setMessage(response.data.message);
      }
    } catch (error) {
      setMessage("회원가입 실패. 다시 시도해주세요.");
    }
  };

  return (
    <div className={styles.register_container}>
      <h1>
        <span className={styles.fit}>FIT</span>
        <span className={styles.track}>Track</span>
      </h1>
      <form onSubmit={handleRegister}>
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
        <button type="submit">회원가입</button>
      </form>
      {message && <p className={styles.message}>{message}</p>}
      <div className={styles.links}>
        <a href="/login">로그인</a>
      </div>
    </div>
  );
};

export default Register;
