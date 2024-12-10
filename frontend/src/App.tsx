import { Routes, Route } from "react-router";
import Home from "@/pages/home";
import Login from "@/pages/login";
import Register from "@/pages/register";
import { Amplify } from "aws-amplify";

Amplify.configure({
  Auth: {
    Cognito: {
      userPoolClientId: "26ovnsjbm9g3feutigk46d38c8",
      userPoolId: "us-east-1_JCbMyyn0b",
      loginWith: {
        email: true,
      },
    },
  },
});

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  );
};

export default App;
