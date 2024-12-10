import { useContext, useState } from "react";
import { useNavigate } from "react-router";
import { AuthContext } from "@/contexts/auth";

const Page = () => {
  const navigate = useNavigate();
  const { signUp } = useContext(AuthContext);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSignUpClick = async () => {
    await signUp({ email, password });

    await navigate("/");
  };

  return (
    <div>
      Sign up
      <div>
        email: <input type="email" value={email} onChange={handleEmailChange} />
      </div>
      <div>
        password:
        <input
          type="password"
          value={password}
          onChange={handlePasswordChange}
        />
      </div>
      <div>
        <button onClick={handleSignUpClick}> Sign up </button>
      </div>
    </div>
  );
};

export default Page;
