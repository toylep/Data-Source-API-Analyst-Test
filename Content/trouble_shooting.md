# Common Issues & Solutions

## 401 Unauthorized:
Verify the personal access token.
Ensure the token has the correct permissions (e.g., repo read access).
## 403 Rate Limit Exceeded:
Use Retry-After header to determine when to retry.
Authenticate to increase rate limits.
## 422 Validation Failed:
Verify that required parameters are passed and correctly formatted.