import { useEffect } from "react";
import { signUp, getCurrentUser, signIn } from "aws-amplify/auth";

const Page = () => {
  useEffect(() => {
    const printUser = async () => {
      const { userId, username } = await getCurrentUser();

      console.log("is cached?", { userId, username });
    };

    printUser();
  });

  const handleSignUpClick = async () => {
    const auth = {
      username: "marcosraul94@gmail.com",
      password: "Hunter2dfgchvbjnkm!@#$%^",
    };

    const { isSignUpComplete, userId } = await signUp(auth);
    console.log({ isSignUpComplete, userId });

    const { isSignedIn } = await signIn(auth);
    console.log({ isSignedIn });
  };

  return (
    <div>
      Home
      <div>
        <button onClick={handleSignUpClick}> Sign up </button>
      </div>
    </div>
  );
};

export default Page;
