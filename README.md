# Engineering Notes

A practical engineering notebook for **MULTEXPK LABS** — commands, experiments, troubleshooting records, architecture decisions, operational lessons, and reusable technical knowledge collected from real software and infrastructure work.

## Purpose

This repository is intentionally different from the larger engineering repositories in the organization. Those repositories provide structured subject-specific engineering references; this one records the **field notes behind the work**.

Typical entry:

**Problem → Evidence → Diagnosis → Change → Verification → Lesson**

## Areas

- Linux, VPS and server operations
- Networking, DNS, Cloudflare and TLS
- PHP and Laravel
- WHMCS and hosting platforms
- MariaDB/MySQL and backend engineering
- WordPress and WooCommerce
- WhatsApp and API automation
- AI, LLMs, Ollama and coding agents
- Deployment, monitoring and reliability
- Debugging and incident analysis
- Architecture decisions
- Experiments and benchmarks
- Reusable commands and checklists

## Evidence-First Engineering

When investigating a problem:

1. **Observe** the actual symptom.
2. **Measure** logs, versions, metrics and state.
3. **Narrow** the failing layer.
4. **Hypothesize** plausible causes.
5. **Test** one meaningful variable at a time.
6. **Verify** the expected result.
7. **Document** the cause, fix and lesson.

A useful layer model is:

`Client → DNS → Edge/Proxy → Network → Web Server → Runtime → Application → Database → External Provider`

## Production Changes

Production notes should identify the exact change, affected service, current state, backup/rollback path, dependencies, verification steps and result.

Prefer the smallest reversible change that can test the hypothesis. For high-risk work, use staging or a controlled rollout first.

See [Production Change Checklist](docs/production-change-checklist.md).

## Architecture Decisions

Use Architecture Decision Records when a decision has meaningful long-term consequences. Record the context, alternatives, decision, trade-offs and verification method rather than only recording the final answer.

See [ADR Template](docs/adr-template.md).

## Research and Reimplementation

MULTEXPK LABS uses:

**Find → Clone → Inspect → Understand → Document → Reimplement → Test → Improve**

Public code and documentation may be studied for architecture and engineering lessons. Licensing, attribution, provider terms and intellectual-property boundaries must be respected. Public demonstrations use synthetic data and never contain production credentials or private customer information.

See [Research Method](docs/research-method.md).

## Resources

- [Engineering note template](docs/note-template.md)
- [Debugging method](docs/debugging-method.md)
- [Production change checklist](docs/production-change-checklist.md)
- [Incident record](docs/incident-record.md)
- [Command notebook](docs/commands.md)
- [ADR template](docs/adr-template.md)
- [Experiment template](templates/experiment-record.md)
- [Change record](templates/change-record.md)
- `bash/quick-system-report.sh` — quick Linux system report
- `python/note_index.py` — index Markdown notes by heading

## Publishing Rules

Before committing a real troubleshooting or operational note, remove:

- API keys and passwords
- Private keys and tokens
- Customer identifiers and contact data
- Production database credentials
- Private IP inventories and sensitive topology
- WhatsApp session/authentication files
- Payment credentials and wallet secrets
- Internal security controls that should not be public

The goal is useful technical education without exposing operational secrets.

## Related MULTEXPK LABS Repositories

- `linux-vps-engine`
- `server-troubleshooting`
- `cloud-infrastructure`
- `php-laravel-engineering`
- `whmcs-engineering`
- `database-backend-engineering`
- `whatsapp-automation`
- `llm-infrastructure`
- `coding-agent-lab`
- `ai-agents-automation`

---

## MULTEXPK LABS

**Zain Ul Abddin — Founder, MULTEXPK LTD ®™**

Technical education first, AI/LLM research second, community and engineering knowledge third, with MULTEXPK infrastructure and cloud services supporting relevant work.

**MULTEXPK LTD ®™ – Secure Cloud • VPS • Hosting • Automation**

https://multexpk.com | https://webvpsserver.com | WhatsApp: +92 312 6565434 | support@multexpk.com