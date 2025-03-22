# Deployment Scenarios

This page outlines three deployment scenarios supported in DC4EU depending on infrastructure constraints and internet access.

## Option A – Dedicated Infrastructure with Direct Internet Access (Production)

- Physical or virtual machine
- Direct internet access on port 443 (HTTPS)
- Public DNS entry required

**Advantages:**
- Straightforward configuration
- Suitable for live services

## Option B – Dedicated Infrastructure without Internet Access (Local Testing)

- Suitable for internal testing
- Uses HTTP (port 80)
- No public DNS, uses `/etc/hosts`

**Limitations:**
- Not suitable for production
- Security limited

## Option C – Reverse Proxy Scenario (Service Provider Environment)

- Uses a public-facing reverse proxy (e.g. Nginx)
- Internal services run behind the proxy
- TLS termination at the proxy level

**Advantages:**
- Enhanced security and load balancing
- Flexible configuration for multi-service setups
