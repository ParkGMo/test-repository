import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import Recommendations from "./pages/Recommendations";
import LogIn from "./loginPage/LogIn";
import Register from "./loginPage/Register";
import DashBoard from "./dashboardPage/DashBoard";
import Workouts from "./workoutPage/Workouts";
import WorkoutDetail from "./workoutPage/WorkoutDetail";
import NewWorkout from "./workoutPage/NewWorkout";
import Profile from "./profilePage/Profile";
import Settings from "./settingPage/Settings";

function App() {
  // return (
  //   <div className="App">
  //     <h1>FitStack</h1>
  //   </div>
  // );
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LogIn />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<DashBoard />} />
        <Route path="/workouts" element={<Workouts />} />
        <Route path="/workouts/:id" element={<WorkoutDetail />} />
        <Route path="/workouts/new" element={<NewWorkout />} />
        {/* <Route path="/body-metrics" element={<BodyMetrics />} /> */}
        {/* <Route path="/recommendations" element={<Recommendations />} /> */}
        <Route path="/profile" element={<Profile />} />
        <Route path="/settings" element={<Settings />} />
        {/* <Route path="*" element={<NotFound />} /> */}
      </Routes>
    </Router>
  );
}

export default App;
