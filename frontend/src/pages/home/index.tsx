import { useContext, useEffect } from "react";
import { AuthContext } from "@/contexts/auth";
import { Link } from "react-router";

const Page = () => {
  const { email, signOut } = useContext(AuthContext);

  useEffect(() => {
    fetch("http://127.0.0.1:2999/unprotected/product");
  }, []);

  return (
    <div>
      Hello {email ? email : ""}
      <ul>
        <li>
          <Link to="/sign-in"> Sign In </Link>
        </li>
        <li>
          <Link to="/sign-up"> Sign Up </Link>
        </li>
      </ul>
      <div>{email && <button onClick={signOut}> Sign out </button>}</div>
    </div>
  );
};

export default Page;
