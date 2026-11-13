# Reading — OIDC to AWS + ECS

## Learning objectives

1. Prefer **GitHub Actions OIDC** over long-lived `AWS_ACCESS_KEY_ID` secrets.
2. Constrain role trust by `sub` (repo + ref).
3. Sketch an ECS Fargate deploy from CI.

## Read these (verified)

1. [GitHub Actions — OIDC with AWS](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
2. [AWS ECS on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
3. [Terraform AWS provider — IAM OIDC](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_openid_connect_provider)

## Next step

`oidc_aws` kata + starter Terraform sketch → quiz.
