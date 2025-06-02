# General Deployment Options

These options determine how Docker is configured depending on your reverse proxy setup.

## Option A – Without Own Reverse Proxy (Recommended)

- All services run within the Docker stack
- HTTPS handled by Docker via Let’s Encrypt
- Default `docker-compose.yml` used

## Option B – With Own Reverse Proxy

- Your infrastructure handles external traffic
- Internal ports must be exposed by each container
- Use `docker-compose-ownReverseProxy.yml` as an example

**Sample NGINX rule:**

```nginx
server {
  server_name uself-issuer-gui.lspgovpart.govpart.de;
  location / {
    proxy_pass http://localhost:9584/;
  }
}
