import { test } from "@jest/globals";
import { render, screen } from "@testing-library/react";
import SignInPage from "@/pages/signIn";

test("Renders the password input", () => {
  render(<SignInPage />);

  screen.getByText(/password/);
});
