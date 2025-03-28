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
import FitnessCategories from "./dashboardPage/FitnessCategories";
import WorkOutList from "./fitnessPage/workOutListPage/WorkOutListPage";
import FitnessPage from "./fitnessPage/FitnessPage";

function App() {
  const notLogin = false;
  return (
    <Router>
      <Routes>
        {notLogin ? (
          <Route path="/">
            <Route index element={<LogIn />} />
            <Route path="register" element={<Register />} />
            <Route path="dashboard" element={<DashBoard />} />
            <Route path="workouts" element={<Workouts />} />
            <Route path="workouts/:id" element={<WorkoutDetail />} />
            <Route path="workouts/new" element={<NewWorkout />} />
            {/* <Route path="body-metrics" element={<BodyMetrics />} /> */}
            {/* <Route path="recommendations" element={<Recommendations />} /> */}
            <Route path="profile" element={<Profile />} />
            <Route path="settings" element={<Settings />} />
            {/* <Route path="*" element={<NotFound />} /> */}
          </Route>
        ) : (
          <Route path="/">
            <Route path="login" element={<LogIn />} />
            <Route path="register" element={<Register />} />
            <Route index element={<DashBoard />} />
            <Route path="workouts" element={<Workouts />} />
            <Route path="workouts/:id" element={<WorkoutDetail />} />
            <Route path="workouts/new" element={<NewWorkout />} />
            <Route path="fitness" element={<FitnessPage />} />
            <Route path="fitnessCategories" element={<FitnessCategories />} />
            <Route path="workOutList" element={<WorkOutList />} />
            {/* <Route path="body-metrics" element={<BodyMetrics />} /> */}
            {/* <Route path="recommendations" element={<Recommendations />} /> */}
            <Route path="profile" element={<Profile />} />
            <Route path="settings" element={<Settings />} />
            {/* <Route path="*" element={<NotFound />} /> */}
          </Route>
        )}
      </Routes>
    </Router>
  );
}

export default App;
