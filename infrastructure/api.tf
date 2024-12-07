module "api_gateway" {
  source = "terraform-aws-modules/apigateway-v2/aws"

  name                  = "test"
  create_domain_name    = false
  create_domain_records = false

  routes = {
    "GET /" = {
      integration = {
        uri                  = module.users_lambda.lambda_function_arn
        timeout_milliseconds = 10000
      }
    }
  }
}

module "users_lambda" {
  source = "terraform-aws-modules/lambda/aws"

  function_name                     = "users"
  handler                           = "app.users"
  runtime                           = "python3.13"
  source_path                       = "../backend"
  publish                           = false
  cloudwatch_logs_retention_in_days = 7

  allowed_triggers = {
    AllowExecutionFromAPIGateway = {
      service    = "apigateway"
      source_arn = "${module.api_gateway.api_execution_arn}/*/*"
    }
  }
}
