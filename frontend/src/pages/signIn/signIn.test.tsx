import { test, jest } from "@jest/globals";
import { render, screen } from "@testing-library/react";
import SignInPage from "@/pages/signIn";

jest.mock("react-router", () => ({ useNavigate: () => jest.fn() }));

test("Renders the password input", () => {
  render(<SignInPage />);

  screen.getByText(/password/);
});
