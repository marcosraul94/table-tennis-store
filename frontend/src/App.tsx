import { Routes, Route } from "react-router";
import Home from "@/pages/home";
import Contact from "@/pages/contact";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/contact" element={<Contact />} />
    </Routes>
  );
};

export default App;
