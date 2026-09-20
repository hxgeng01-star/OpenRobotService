# Self-hosted Runner for UI Regression

## Purpose

The UI regression runner is installed on the test server so jobs execute in the same network namespace as:

```text
127.0.0.1:9400
127.0.0.1:9411
127.0.0.1:3306
```

This avoids routing test traffic through a public SSH tunnel from a GitHub-hosted runner.

## Runner

```text
name: ors-test-ecm-3bca
labels: self-hosted, linux, x64, ors-test
directory: /home/usp-a/actions-runner
service: actions-runner.service (user systemd)
```

## Workflow

```yaml
runs-on: [self-hosted, linux, x64, ors-test]
```

UI regression uses direct local URLs:

```text
UI_REGRESSION_DIRECT=1
UI_REGRESSION_BACKEND_URL=http://127.0.0.1:9400
UI_REGRESSION_AI_URL=http://127.0.0.1:9411
UI_REGRESSION_DB_HOST=127.0.0.1
UI_REGRESSION_DB_PORT=3306
```

## Checkout

The fork practice workflow avoids a full Git checkout because the test server's
GitHub TLS connection was unstable. It downloads a trimmed archive containing
only the directories required by UI regression:

```text
.github/
automation/
frontend/
```

The archive is stored for fork practice at:

```text
automation/testdata/bootstrap/ui-regression-src.tar.gz
```

This is a practice-only workaround. The production repository should use a
stable runner/network path or a local Git mirror instead of committing a
generated archive.

## Required Secrets

Configure these in the fork repository:

```text
REAL_U1_PASSWORD
REAL_U2_PASSWORD
UI_REGRESSION_CLEANUP_PASSWORD
```

`UI_REGRESSION_DB_PASSWORD` is only required when database compensation cleanup is enabled.

## Security

Do not run self-hosted workflows for untrusted pull requests. Keep the UI Regression trigger limited to trusted branch pushes and manual dispatch.
