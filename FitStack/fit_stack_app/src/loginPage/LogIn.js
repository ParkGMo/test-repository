import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { motion } from "framer-motion";
import axios from "axios";
// import { Input } from "@/components/ui/input";
// import { Button } from "@/components/ui/button";

function LogIn() {
  // return <div>LogIn</div>;
  const [loginData, setLoginData] = useState({
    identifier: "", // 닉네임 또는 이메일
    password: "",
  });
  const [workouts, setWorkouts] = useState([]);

  const handleChange = (e) => {
    setLoginData({ ...loginData, [e.target.name]: e.target.value });
  };

  const handleLogin = () => {
    console.log("로그인 시도: ", loginData);
    // 실제 로그인 API 연동 필요
  };

  useEffect(() => {
    axios
      // .get("http://localhost:5000/workouts")
      .get("http://localhost:5000")
      .then((response) => {
        setWorkouts(response.data);
      })
      .catch((error) => {
        console.error("데이터 불러오기 실패:", error);
      });
  }, []);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      {/* 애니메이션 타이틀 */}
      <motion.h1
        className="text-4xl font-bold mb-6"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
      >
        <motion.span
          className="text-blue-500"
          animate={{ rotateY: [0, 360] }}
          transition={{ repeat: Infinity, duration: 2 }}
        >
          FIT
        </motion.span>
        -
        <motion.span
          className="text-green-500"
          animate={{ rotateX: [0, 360] }}
          transition={{ repeat: Infinity, duration: 2 }}
        >
          Track
        </motion.span>
      </motion.h1>

      {/* 로그인 폼 */}
      <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
        {/* <Input
          type="text"
          name="identifier"
          placeholder="닉네임 또는 이메일"
          value={loginData.identifier}
          onChange={handleChange}
          className="mb-4"
        />
        <Input
          type="password"
          name="password"
          placeholder="비밀번호"
          value={loginData.password}
          onChange={handleChange}
          className="mb-4"
        />
        <Button onClick={handleLogin} className="w-full mb-2">
          로그인
        </Button>
        <Link
          to="/forgot-password"
          className="text-sm text-blue-500 hover:underline"
        >
          비밀번호를 잊으셨나요?
        </Link> */}
      </div>
    </div>
  );
}

export default LogIn;
