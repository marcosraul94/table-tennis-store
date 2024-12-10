import { Routes, Route } from "react-router";
import Home from "@/pages/home";
import SignIn from "@/pages/signIn";
import SignUp from "@/pages/signUp";


const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/sign-in" element={<SignIn />} />
      <Route path="/sign-up" element={<SignUp />} />
    </Routes>
  );
};

export default App;
