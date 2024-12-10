import "./index.css";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router";
import { Amplify } from "aws-amplify";
import App from "@/App";
import { cognitoConfig } from "@/utils/env";
import { AuthProvider } from "@/contexts/auth";

Amplify.configure({
  Auth: { Cognito: cognitoConfig },
});

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <AuthProvider>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </AuthProvider>
  </StrictMode>
);
