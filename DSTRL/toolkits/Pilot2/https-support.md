```markdown
# HTTPS Support Configuration

This guide explains how to enable or disable HTTPS support for your DC4EU Docker deployment environment. HTTPS is required for secure communication with wallets and external services, particularly when integrating with the EBSI infrastructure, the EUDI Wallet, and identity-related components.

## 🔐 When to Use HTTPS

HTTPS must be enabled in the following scenarios:

- Production or pilot environments exposed to the public internet
- Credential issuance or verification through wallets
- Integration with EBSI trust services and public DNS

## 🔧 Configuration Overview

HTTPS is enabled using **Let's Encrypt** certificates, automatically provisioned through environment variables set in the `docker-compose.yml` file.

To activate HTTPS support:

1. Ensure your DNS entries are properly configured and resolvable (see [deployment-scenarios.md](./deployment-scenarios.md))
2. Confirm that **port 443** is open and accessible
3. Uncomment the relevant `LETSENCRYPT_HOST` and `VIRTUAL_HOST` entries in your `docker-compose.yml` file

## ✅ Enabling HTTPS (Recommended for Production)

Open your `docker-compose.yml` file and ensure the following lines are **not commented** (no `#` prefix):

```yaml
environment:
  - VIRTUAL_HOST=uself-issuer-gui.lsp[ORG].domain
  - LETSENCRYPT_HOST=uself-issuer-gui.lsp[ORG].domain
  - LETSENCRYPT_EMAIL=admin@[ORG].domain
```

Repeat this configuration for each relevant container (e.g. `issuer-gui`, `verifier-gui`, `pid-generator`, etc.).

### 🔄 Example

```yaml
services:
  uself-issuer-gui:
    environment:
      - VIRTUAL_HOST=uself-issuer-gui.lspgovpart.govpart.de
      - LETSENCRYPT_HOST=uself-issuer-gui.lspgovpart.govpart.de
      - LETSENCRYPT_EMAIL=admin@govpart.de
```

---

## 🧪 Disabling HTTPS (Testing Only)

If deploying locally or in an internal-only test environment, HTTPS can be disabled. To do so:

1. Comment out all `LETSENCRYPT_HOST` and `LETSENCRYPT_EMAIL` lines
2. Ensure `PROTOCOL=http` is defined in your `.env` file

### Example for HTTP:

```yaml
services:
  uself-issuer-gui:
    environment:
      - VIRTUAL_HOST=uself-issuer-gui.lspgovpart.govpart.de
      # - LETSENCRYPT_HOST=uself-issuer-gui.lspgovpart.govpart.de
      # - LETSENCRYPT_EMAIL=admin@govpart.de
```

And in `.env`:
```env
PROTOCOL=http
```

> ⚠️ **Warning:** HTTP should never be used in production or any publicly accessible environment.

---

## 📄 Related Files

- `.env` — Defines protocol and domain
- `docker-compose.yml` — Controls environment variables for HTTPS
- `docker-compose-ownReverseProxy.yml` — If using external reverse proxy (TLS handled externally)

---

## 🛠️ Troubleshooting

If HTTPS is not working as expected:

- Verify DNS resolution (`ping uself-issuer-gui.lsp[ORG].domain`)
- Check firewall rules for port 443
- Review logs with `docker compose logs -f` for certificate errors
- Inspect the Let's Encrypt volume if certificates are not being generated

---

**© 2023–2025 DC4EU** – Co-funded by the European Union's Digital Europe Programme under Grant Agreement no. 101102611
```
