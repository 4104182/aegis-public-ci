# Aegis wallet — PUBLIC synthetic CI

This is an **independent PUBLIC testing repository** for Aegis wallet. It contains only invented public fixtures and example test functions. It is intentionally **not** a copy of the proprietary/private application.

**Testing scope:** Simulated fail-closed owner/network-gate contract. It does not exercise Aegis application code, JNI, a VPN, a wallet, or real cryptography.

GitHub Actions checks source files in **this public repository only** and runs five Python standard-library tests. It does not clone, fetch, import, or decrypt the matching private repository; no secrets or production keys are configured.

- Project source, full Git history, debug/test APK, internal QA receipts: PRIVATE GitHub.
- GitHub-hosted synthetic CI: THIS PUBLIC repository.
- Real build/device/native security tests: temporary owner-authorized build/test servers, from a pinned PRIVATE commit.
- Result label: `PUBLIC_SYNTHETIC_PASS`, not an application build or real cryptographic test.

See [AGENTS.md](./AGENTS.md) for the public/private boundary. Do not create public GitHub assets from private code or server data.
