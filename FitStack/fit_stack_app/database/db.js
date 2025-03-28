const express = require("express");
const mysql = require("mysql");
const cors = require("cors");
require("dotenv").config();

const app = express();
// app.use(cors()); // CORS 허용
app.use(
  cors({
    origin: "http://localhost:3000", // 리액트 주소
    methods: ["GET", "POST"],
    credentials: true,
  })
);
app.use(express.urlencoded({ extended: true })); // URL 인코딩된 데이터 파싱
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

app.post("/api/register", async (req, res) => {
  try {
    const { username, email, password, age, gender, height_cm, weight_kg } =
      req.body;

    if (!username || !email || !password) {
      return res.status(400).json({ error: "필수 입력값이 없습니다." });
    }

    // 비밀번호 해싱
    const saltRounds = 10;
    const hashedPassword = await bcrypt.hash(password, saltRounds);

    // SQL 쿼리 실행
    const sql = `INSERT INTO fit_user (username, email, password_hash, age, gender, height_cm, weight_kg) VALUES (?, ?, ?, ?, ?, ?, ?)`;
    const values = [
      username,
      email,
      hashedPassword,
      age || null,
      gender || null,
      height_cm || null,
      weight_kg || null,
    ];

    db.query(sql, values, (err, result) => {
      if (err) {
        console.error("회원가입 오류:", err);
        return res.status(500).json({ error: "회원가입 실패" });
      }
      res.json({ message: "회원가입 성공!" });
    });
  } catch (error) {
    console.error("회원가입 오류:", error);
    res.status(500).json({ error: "서버 오류" });
  }
});

// app.post("/fit_user", (req, res) => {
//   const { username, email, password, age, gender, height_cm, weight_kg } =
//     req.body;

//   // 비밀번호 해시 (saltRounds = 10)
//   bcrypt.hash(password, 10, (err, hash) => {
//     if (err) {
//       return res.status(500).json({ error: "비밀번호 해싱 실패" });
//     }

//     // MySQL에 저장
//     const sql = `INSERT INTO fit_user (username, email, password_hash, age, gender, height_cm, weight_kg) VALUES (?, ?, ?, ?, ?, ?, ?)`;
//     const values = [username, email, hash, age, gender, height_cm, weight_kg];

//     db.query(sql, values, (err, result) => {
//       if (err) {
//         return res.status(500).json({ error: "회원가입 실패" });
//       }
//       res.json({ message: "회원가입 성공!" });
//     });
//   });
// });

// 서버 실행
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`서버 실행 중: http://localhost:${PORT}`);
});

// 해당 파일 이동후 -> node 파일명작성 하면 서버 연결!!
