module "api_gateway" {
  source = "terraform-aws-modules/apigateway-v2/aws"

  name                  = "table_tennis_store"
  create_domain_name    = false
  create_domain_records = false

  routes = {
    "ANY /" = {
      integration = {
        uri                  = module.api_lambda.lambda_function_arn
        timeout_milliseconds = 10000
      }
    }
  }
}

module "api_lambda" {
  source = "terraform-aws-modules/lambda/aws"

  function_name                           = "table_tennis_store_api"
  handler                                 = "app.users"
  runtime                                 = "python3.13"
  source_path                             = "../backend/api"
  publish                                 = false
  cloudwatch_logs_retention_in_days       = 7
  create_current_version_allowed_triggers = false

  allowed_triggers = {
    AllowExecutionFromAPIGateway = {
      service    = "apigateway"
      source_arn = "${module.api_gateway.api_execution_arn}/*/*"
    }
  }
}
