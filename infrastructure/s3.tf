module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket                  = "rumv-table-tennis-store-host"
  force_destroy           = true
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false

  versioning = {
    enabled = false
  }
}

resource "aws_s3_bucket_website_configuration" "website-configuration" {
  bucket = module.s3_bucket.s3_bucket_id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}

resource "aws_s3_bucket_policy" "public_read_policy" {
  bucket = module.s3_bucket.s3_bucket_id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Sid       = "PublicReadGetObject",
        Effect    = "Allow",
        Principal = "*",
        Action    = "s3:GetObject",
        Resource  = "${module.s3_bucket.s3_bucket_arn}/*"
      }
    ]
  })
}
