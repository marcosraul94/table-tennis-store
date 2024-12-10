import { CognitoUserPoolConfig } from "@aws-amplify/core";
import { ENV } from "@/utils/enum";

// export const env = (process.env.ENV as ENV) || ENV.LOCAL;
export const env = ENV.LOCAL;

const devCongitoConfig = {
  userPoolClientId: "26ovnsjbm9g3feutigk46d38c8",
  userPoolId: "us-east-1_JCbMyyn0b",
};

const cognitoConfigByEnv = {
  [ENV.TEST]: {},
  [ENV.LOCAL]: devCongitoConfig,
  [ENV.DEV]: devCongitoConfig,
  [ENV.PROD]: devCongitoConfig,
};

export const cognitoConfig = cognitoConfigByEnv[env] as CognitoUserPoolConfig;
