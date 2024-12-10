import { createContext, useState, useEffect, ReactNode } from "react";
import {
  getCurrentUser,
  signUp as baseSignUp,
  signIn as baseSignIn,
  signOut as baseSignOut,
} from "aws-amplify/auth";

export interface AuthCredentials {
  email: string;
  password: string;
}

export interface AuthContextProps {
  isAuthenticated: boolean;
  email: string | null;
  isLoading: boolean;
  signUp: (credentials: AuthCredentials) => Promise<void>;
  signIn: (credentials: AuthCredentials) => Promise<void>;
  signOut: () => Promise<void>;
}

export interface AuthProviderProps {
  children: ReactNode;
}

export const AuthContext = createContext<AuthContextProps>({
  isAuthenticated: false,
  email: null,
  isLoading: true,
  signUp: async () => {},
  signIn: async () => {},
  signOut: async () => {},
});

export const AuthProvider = ({ children }: AuthProviderProps) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [email, setEmail] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const loadCachedUser = async () => {
      setIsLoading(true);

      try {
        const { signInDetails } = await getCurrentUser();
        if (!signInDetails?.loginId) return;

        setEmail(signInDetails.loginId);
        setIsAuthenticated(true);
      } catch {
        return;
      } finally {
        setIsLoading(false);
      }
    };

    loadCachedUser();
  }, []);

  const signOut = async () => {
    await baseSignOut();

    setEmail(null);
    setIsAuthenticated(false);
  };

  const signIn = async (credentials: AuthCredentials) => {
    setIsLoading(true);

    try {
      if (email) await signOut();

      await baseSignIn({
        username: credentials.email,
        password: credentials.password,
      });

      setEmail(credentials.email);
      setIsAuthenticated(true);
    } finally {
      setIsLoading(false);
    }
  };

  const signUp = async (credentials: AuthCredentials) => {
    try {
      if (email) await signOut();

      await baseSignUp({
        username: credentials.email,
        password: credentials.password,
      });

      await signIn(credentials);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <AuthContext.Provider
      value={{ email, isAuthenticated, signIn, signUp, isLoading, signOut }}
    >
      {children}
    </AuthContext.Provider>
  );
};
