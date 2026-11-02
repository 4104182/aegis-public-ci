# PUBLIC CI AGENTS — Aegis wallet

This repository is PUBLIC and every commit, workflow, artifact and log must be safe for anyone to read.

**Strict separation:** PRIVATE application source code, internal APKs, sensitive QA, history, credentials and exact host/account inventory remain in an authorized PRIVATE GitHub repository, never this one. Only independently written synthetic tests and deliberately publishable interfaces are allowed here. DO NOT clone or checkout any PRIVATE repository in GitHub Actions, make private repos public, include GitHub credentials beyond read-only default GITHUB_TOKEN, or upload private test outputs. Avoid customer/payment/user content, signing material, mnemonics, device identifiers and server credentials.

**Execution model:** synthetic GitHub-hosted jobs run ONLY in this PUBLIC repository. Actual application builds, native crypto, Android emulator and real integration tests are performed separately on disposable owner-authorized servers from pinned PRIVATE GitHub source; test APKs must be returned to PRIVATE GitHub as gated QA assets. Successful synthetic tests are **PUBLIC_SYNTHETIC_PASS** only, never production readiness.

**Purpose for this project:** Simulated fail-closed owner/network-gate contract. It does not exercise Aegis application code, JNI, a VPN, a wallet, or real cryptography.

Instructions for five RDC identities, 6 hosts, per-user source inventory and migration coordination stay in the PRIVATE coordinating AGENTS.md and automations, not in public workflow logs.
