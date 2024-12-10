import { signUp } from "aws-amplify/auth";

const Page = () => {
  const handleSignUpClick = async () => {
    const { isSignUpComplete, userId, nextStep } = await signUp({
      username: "marcosraul94@gmail.com",
      password: "Hunter2dfgchvbjnkm!@#$%^",
    });

    console.log({ isSignUpComplete, userId, nextStep });
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
