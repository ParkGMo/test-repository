const express = require("express");
const mysql = require("mysql");
const cors = require("cors");
require("dotenv").config();

const app = express();
app.use(cors()); // CORS 허용
app.use(express.json()); // JSON 요청 처리

// MySQL 연결 설정
const db = mysql.createConnection({
  host: "localhost",
  port: "3306",
  user: "root",
  password: "1234",
  database: "fittrack",
});

db.connect((err) => {
  if (err) {
    console.error("MySQL 연결 실패:", err);
  } else {
    console.log("MySQL 연결 성공!");
  }
});

// 유저 기록 가져오기 API
app.get("/fit_user", (req, res) => {
  const sql = "SELECT * FROM fit_user";
  db.query(sql, (err, results) => {
    if (err) {
      res.status(500).send(err);
    } else {
      res.json(results);
    }
  });
});

// 회원가입 API (라우터 없이 직접 정의)
// app.post("/register", async (req, res) => {
app.post("/api/register", async (req, res) => {
  const {
    user_id,
    username,
    email,
    hashedPassword,
    age,
    gender,
    height_cm,
    weight_kg,
    created_at,
    updated_at,
    deleted_at,
  } = req.body;

  try {
    // 비밀번호 해싱
    const saltRounds = 10;
    const hashedPassword = await bcrypt.hash(password, saltRounds);

    const sql = `
      INSERT INTO fit_user (user_id, username, email, password_hash, age, gender, height_cm, weight_kg, created_at, updated_at, deleted_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
      `;

    mysql.query(
      sql,
      [
        user_id,
        username,
        email,
        hashedPassword,
        age,
        gender,
        height_cm,
        weight_kg,
        created_at,
        updated_at,
        deleted_at,
      ],
      (err, result) => {
        if (err) {
          console.error("회원가입 실패:", err);
          return res
            .status(500)
            .json({ message: "회원가입 중 오류가 발생했습니다." });
        }
        res.status(201).json({ message: "회원가입 성공!" });
      }
    );
  } catch (error) {
    console.error("서버 오류:", error);
    res.status(500).json({ message: "서버 오류 발생" });
  }
});

// 서버 실행
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`서버 실행 중: http://localhost:${PORT}`);
});

// 해당 파일 이동후 -> node 파일명작성 하면 서버 연결!!
