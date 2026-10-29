# Remediation Plan

## Fixes Applied

### Fix 1: JWT none Algorithm Removed - CRITICAL
- **File:** app/auth.py (line 38)
- **Before:** algorithms=[ALGORITHM, 'none']
- **After:** algorithms=[ALGORITHM]
- **Risk Eliminated:** Attackers can no longer forge unsigned JWT tokens.

### Fix 2: SQL Injection Remediated - CRITICAL
- **File:** app/database.py (lines 20-27)
- **Before:** Raw f-string SQL query construction
- **After:** SQLAlchemy ORM with parameterized .ilike() filters
- **Risk Eliminated:** User input is no longer interpolated into raw SQL.

### Fix 3: Hardcoded Secrets Removed - HIGH
- **File:** app/config.py
- **Before:** Plaintext SECRET_KEY, DB_PASSWORD, ADMIN_API_KEY in source
- **After:** All secrets loaded from environment variables via os.environ.get()
- **Risk Eliminated:** Secrets no longer exposed in version control.

## Remaining Items (Backlog)

| Finding | Priority | Estimated Effort |
|---------|----------|-----------------|
| Broken access control | HIGH | 2 hours |
| SSRF webhook validation | HIGH | 1 hour |
| Password logging removal | HIGH | 30 min |
| Verbose error handlers | MEDIUM | 1 hour |
| CORS restriction | MEDIUM | 30 min |
| Notification service auth | MEDIUM | 2 hours |
