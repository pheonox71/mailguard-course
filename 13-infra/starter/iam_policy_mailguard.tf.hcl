# Equivalent least-privilege policy as HCL (aws_iam_policy_document style).
# Replace YOUR_SECURE_DROP_BUCKET / ACCOUNT_ID / REGION before use.
# Why not s3:* or sqs:* on "*": a compromised worker must not reach unrelated
# buckets/queues or IAM APIs.

data "aws_iam_policy_document" "mailguard_runtime_least_privilege" {
  statement {
    sid    = "SecureDropObjects"
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:PutObject",
      "s3:DeleteObject",
    ]
    resources = ["arn:aws:s3:::YOUR_SECURE_DROP_BUCKET/*"]
  }

  statement {
    sid    = "SecureDropListBucket"
    effect = "Allow"
    actions = [
      "s3:ListBucket",
    ]
    resources = ["arn:aws:s3:::YOUR_SECURE_DROP_BUCKET"]
  }

  statement {
    sid    = "HoldQueueConsume"
    effect = "Allow"
    actions = [
      "sqs:ReceiveMessage",
      "sqs:DeleteMessage",
      "sqs:GetQueueAttributes",
      "sqs:ChangeMessageVisibility",
    ]
    resources = ["arn:aws:sqs:REGION:ACCOUNT_ID:mailguard-hold-dev"]
  }
}
