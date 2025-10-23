# AWS IAM List Users: Bridging GRC and Cloud through AI and Automation

## Concept Overview

This mini-project demonstrates how Governance, Risk, and Compliance (GRC) practitioners can use AI-assisted reasoning and Python automation to connect regulatory controls (NIST SP 800-53) directly to AWS evidence.

Instead of manually reading documentation or writing scripts from scratch, we used Ollama (a local AI runtime) with the HackIDLE-NIST-Coder model (a NIST-aligned reasoning assistant) to generate a compliant, minimal Python example.

---

## Tools & Setup

| Tool                    | Purpose                                                         |
| ------------------------| --------------------------------------------------------------- |
| **Ollama**              | Local AI engine to run the `etgohome/hackidle-nist-coder` model |
| **HackIDLE-NIST-Coder** | AI model fine-tuned for NIST cybersecurity publications         |
| **AWS (IAM)**           | Source of account management data                               |
| **Python + boto3**      | Programmatic access to AWS APIs                                 |

---

## Step-by-Step Setup

1. Run the AI model locally
```bash
ollama pull etgohome/hackidle-nist-coder
ollama run etgohome/hackidle-nist-coder
```
Example query inside Ollama:
```pgsql
>>> Write a minimal Python script using boto3 to list IAM users in my AWS account.
>>> Add two short comments linking the purpose to NIST 800-53 AC-2 (Account Management).
```

2. Save the generated script locally
```bash
mkdir mini-project-iam-list-users
cd mini-project-iam-list-users
nano iam_list_users.py
```

3. Run the script
```bash
python iam_list_users.py --profile angie
```

Optional details mode:
```
python iam_list_users.py --profile angie --details
```

## Example Output
```yaml
List of IAM Users:
annie.crane | ID: AIDAV2H00TS0BOJID0002 | ARN: arn:aws:iam::300066700000:user/annie.crane | Created: 2025-09-11 02:21:42
...
```

---

## NIST SP 800-53 Linkage

| Control  | Title              | Purpose                                                       | How This Script Helps                                   |
| -------- | ------------------ | ------------------------------------------------------------- | ------------------------------------------------------- |
| **AC-2** | Account Management | Ensure accounts are created, managed, and removed per policy. | Lists all IAM users for visibility and control testing. |

---

## GRC “Soft Skill” Perspective

Learning to code for GRC isn’t about becoming a developer. It’s about learning to speak the language of the cloud.

By using tools like Ollama and boto3, you are:

- Asking the cloud direct questions (“Who are my users?”)
- Verifying compliance automatically
- Reducing manual audit overhead

---
