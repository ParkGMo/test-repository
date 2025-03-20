const db = require("../config/db"); // MySQL 연결 정보
const bcrypt = require("bcrypt"); // 비밀번호 해싱 비교용
const jwt = require("jsonwebtoken"); // JWT 토큰 생성용

// JWT 토큰 시크릿 키
const SECRET_KEY = "your_secret_key"; // 환경 변수로 관리하는 것이 좋음!

// 🔹 로그인 컨트롤러
exports.loginUser = (req, res) => {
  const { email, password } = req.body;

  // 입력값 검증
  if (!email || !password) {
    return res.status(400).json({ message: "이메일과 비밀번호를 입력하세요!" });
  }

  // 1️⃣ MySQL에서 사용자 조회
  const sql = "SELECT * FROM users WHERE email = ?";
  db.query(sql, [email], (err, result) => {
    if (err) {
      console.error("DB 오류:", err);
      return res.status(500).json({ error: "서버 오류" });
    }

    if (result.length === 0) {
      return res.status(401).json({ message: "이메일이 존재하지 않습니다!" });
    }

    const user = result[0];

    // 2️⃣ 비밀번호 검증 (bcrypt 비교)
    bcrypt.compare(password, user.password, (err, isMatch) => {
      if (err) {
        console.error("비밀번호 비교 오류:", err);
        return res.status(500).json({ error: "서버 오류" });
      }

      if (!isMatch) {
        return res
          .status(401)
          .json({ message: "비밀번호가 올바르지 않습니다!" });
      }

      // 3️⃣ JWT 토큰 발급
      const token = jwt.sign(
        { userId: user.id, email: user.email, nickname: user.nickname },
        SECRET_KEY,
        { expiresIn: "2h" } // 토큰 유효기간 2시간
      );

      res.status(200).json({ message: "로그인 성공!", token, user });
    });
  });
};
