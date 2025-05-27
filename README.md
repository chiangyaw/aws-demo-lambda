# Vulnerable AWS Lambda Deployment

This project deploys an intentionally vulnerable AWS Lambda function integrated with an API Gateway using Terraform. The function is designed for security testing purposes, enabling you to practice exploiting common vulnerabilities like SQL Injection and Command Injection.

> **Warning:** This deployment is for educational and testing purposes only. Do not use in production or expose it to public networks. Deploy in a controlled, isolated environment.

---

## How It Works

1. **Lambda Function**:
   - A Python-based Lambda function (`lambda_function.py`) is deployed, containing deliberately a simple and vulnerable code.

2. **API Gateway**:
   - Exposes the Lambda function as an HTTP API.
   - The API Gateway automatically passes query parameters to the Lambda function for processing.

3. **Terraform Automation**:
   - Terraform automates the deployment of the following AWS resources:
     - IAM Role and Policies for Lambda execution.
     - Lambda function with the vulnerable code.
     - API Gateway HTTP API with integration to the Lambda function.
    Optional: Using Terraform is optional, you can choose to deploy the items manually. 

---

## Prerequisites

- **Terraform**: Installed on your local machine. [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- **AWS CLI**: Configured with credentials and a default region. [Install AWS CLI](https://aws.amazon.com/cli/)
- **ZIP Utility**: To package the Lambda function code (`lambda_function.py`).

---

## Usage Instructions

### Step 1: Prepare the Lambda Function Code
1. Save the vulnerable Lambda function code as `lambda_function.py`.
2. Create a ZIP file for the function:
   ```
   zip function.zip lambda_function.py
   ```

### Step 2: Deploy the Infrastructure
1. Initialize Terraform:
   ```
   terraform init
   ```

2. Deploy the resources:
    ```
    terraform apply
    ```

3. Confirm the deployment when prompted.

4. Note the API Gateway endpoint displayed in the output.

### Step 3: Test the Vulnerability

## Clean Up
To avoid unnecessary costs, destroy the infrastructure after testing:
```
terraform destroy
```

## Important Notes
* Deploy in an isolated environment (e.g., private VPC or local AWS account).
* This project is intended for ethical security testing only.
* Never expose this setup to the public internet.
* Always clean up resources after testing.

## Disclaimer
This project is intended for educational purposes only. The authors are not responsible for any misuse of this code or any unintended consequences resulting from its deployment.
