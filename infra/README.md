# infra/ -- IaC test data

Infrastructure-as-code for the **IaC Security** and **Static Code Analysis / IaC Security
Scanning** checks (checkov, tfsec, KICS). These templates are scanner fixtures, **not
deployable infrastructure**: every resource carries a deliberate misconfiguration and none
holds credentials. Nothing here is Python, imported, or tested.

| File | Format | Planted findings |
|---|---|---|
| `terraform/orderlab-aws.tf` | Terraform | security group open to `0.0.0.0/0` on 22, 3389 and all ports; public-read-write S3 bucket with public access block off; unencrypted EBS, RDS, SQS and EC2 root volume; public RDS; IMDSv1; HTTP load balancer; IAM `*:*`; CloudTrail without validation; KMS key without rotation; weak password policy |
| `cloudformation/orderlab-aws.yaml` | AWS CloudFormation | public S3 bucket, security group open to the internet, public unencrypted RDS, unencrypted EBS, wildcard IAM policy |
| `kubernetes/orderlab-api.yaml` | Kubernetes | privileged root container, host network/PID, `:latest` image, no limits, LoadBalancer open to all, `cluster-admin` binding |

| Report classification | Evidence here |
|---|---|
| Open Security Group Rule Detection / Open Network Access | security groups and NACL open to the internet |
| Unencrypted Storage Definition / Storage Encryption Gap | unencrypted RDS, EBS, SQS, EC2 volume |
| Publicly Exposed Resource Detection / Public Exposure Risk | public S3, public RDS, internet-facing LB |
| CIS Benchmark Compliance / CIS Compliance Gap | CloudTrail, KMS rotation, password policy, wildcard IAM |
