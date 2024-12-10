resource "aws_cognito_user_pool" "pool" {
  name = "table tennis store pool"

  mfa_configuration        = "OFF"
  username_attributes      = ["email"]
  auto_verified_attributes = []

  lambda_config {
    pre_sign_up = module.pre_sign_up_lambda.lambda_function_arn
  }
}

resource "aws_cognito_user_pool_client" "client" {
  name = "table tennis store client"

  user_pool_id = aws_cognito_user_pool.pool.id
}

module "pre_sign_up_lambda" {
  source = "terraform-aws-modules/lambda/aws"

  function_name                           = "pre_sign_up_cognito"
  handler                                 = "preSignUp.handler"
  runtime                                 = "nodejs22.x"
  source_path                             = "../cognito"
  publish                                 = false
  cloudwatch_logs_retention_in_days       = 7
  create_current_version_allowed_triggers = false

  allowed_triggers = {
    AllowExecutionFromCognito = {
      principal  = "cognito-idp.amazonaws.com"
      source_arn = aws_cognito_user_pool.pool.arn
    }
  }
}