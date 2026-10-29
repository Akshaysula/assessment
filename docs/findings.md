# Security Findings Report

## Scan Summary

| Scan Type | Tool | Findings |
|-----------|------|----------|
| SAST | Bandit | 4 issues |
| SCA | pip-audit | 67 vulnerabilities in 8 packages |
| IaC | Trivy config | 1 Dockerfile scanned |
| Container/Deps | Trivy fs | Dependencies scanned |

## Critical / High Findings

### 1. SQL Injection (CWE-89) - CRITICAL
- **File:** app/database.py (lines 22-26)
- **Tool:** Bandit (B608)
- **Description:** User input is interpolated directly into SQL query via f-string allowing SQL injection.
- **Impact:** Attacker can read modify or delete any data in the database.

### 2. JWT none Algorithm Accepted (CWE-345) - CRITICAL
- **File:** app/auth.py (line 44)
- **Tool:** Manual Review
- **Description:** JWT decode accepts the none algorithm allowing attackers to forge tokens without a secret key.
- **Impact:** Complete authentication bypass.

### 3. Hardcoded Secrets (CWE-259) - HIGH
- **File:** app/config.py (lines 3, 9, 10)
- **Tool:** Bandit (B105)
- **Description:** SECRET_KEY, DB_PASSWORD and ADMIN_API_KEY are hardcoded in source code.
- **Impact:** Secrets exposed in version control.

### 4. Broken Access Control (CWE-284) - HIGH
- **File:** app/main.py
- **Tool:** Manual Review
- **Description:** Users can update or delete scans owned by other users with no ownership check.
- **Impact:** Any authenticated user can modify other users data.

### 5. SSRF via Webhook URL (CWE-918) - HIGH
- **File:** notify/src/index.js
- **Tool:** Manual Review
- **Description:** Webhook registration accepts arbitrary URLs without validation.
- **Impact:** Attacker can probe internal network services.

### 6. Password Logged in Plaintext (CWE-532) - HIGH
- **File:** app/main.py (registration endpoint)
- **Tool:** Manual Review
- **Description:** User password is logged during registration.
- **Impact:** Credentials exposed in log files.

## Medium Findings

### 7. Verbose Error Handlers - MEDIUM
- **File:** app/main.py
- **Description:** Exception handlers return full stack traces to clients leaking internal details.

### 8. Permissive CORS - MEDIUM
- **File:** app/main.py
- **Description:** CORS allows all origins enabling cross-site attacks.

### 9. No Auth on Notification Service - MEDIUM
- **File:** notify/src/index.js
- **Description:** Notification endpoints have no authentication.

## SCA Vulnerabilities

Found 67 known vulnerabilities across 8 packages. Full details in reports/pip-audit.json.
