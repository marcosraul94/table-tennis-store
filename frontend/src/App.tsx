import { Routes, Route } from "react-router";
import Home from "@/pages/home";
import Login from "@/pages/login";
import Register from "@/pages/register";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/login" element={<Register />} />
    </Routes>
  );
};

export default App;
