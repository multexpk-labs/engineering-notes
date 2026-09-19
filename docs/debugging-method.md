# Evidence-First Debugging

A reusable debugging workflow:

1. **Observe** — reproduce the symptom.
2. **Measure** — collect logs, status, metrics, and versions.
3. **Narrow** — isolate the failing layer.
4. **Hypothesize** — identify plausible causes.
5. **Test** — change one meaningful variable at a time.
6. **Verify** — confirm the expected behavior.
7. **Document** — record the cause and fix.

## Layer model

Client → DNS → Edge/Proxy → Network → Web Server → Runtime → Application → Database → External Provider

The same method applies to VPS incidents, Laravel errors, WHMCS failures, API integrations, AI endpoints, and messaging systems.

Avoid destructive troubleshooting when a read-only diagnostic can answer the question first.
