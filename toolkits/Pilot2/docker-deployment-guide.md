# DC4EU Docker Deployment Guide

This repository provides the necessary resources and instructions to deploy the DC4EU piloting agents using Docker. The deployment supports multiple infrastructure configurations and includes HTTPS support for production environments.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Repository Download](#repository-download)
- [Docker Configuration](#docker-configuration)
- [Environment and Deployment Files](#environment-and-deployment-files)
- [Deployment and Verification](#deployment-and-verification)

For advanced configuration options, refer to:
- [Deployment Scenarios](./deployment-scenarios.md)
- [General Deployment Options](./deployment-options.md)
- [Environment File Configuration](./environment-config.md)
- [HTTPS Support Configuration](./https-support.md)

---

## Introduction

This guide describes the steps required to deploy the DC4EU educational piloting environment using Docker Compose. The setup is intended for technical teams supporting testing, integration, and live scenarios for the DC4EU wallet, agents, and supporting services.

## Prerequisites

**Infrastructure requirements:**
- 4 CPU cores
- 16 GB RAM
- 150 GB free disk space

**Software dependencies:**
- Docker
- Docker Compose
- Git

**Verify installations:**
```bash
docker -v
docker compose version
git --version
```

**Git repository access:**
Ensure your GitHub username and email have been shared with your organisation's SPOC and WP5 coordination to obtain access to the private `educational-pilot-deployment` repository.

## Repository Download

Navigate to the directory where you want to store the project and clone the repository.

**Option A (with Personal Access Token, for GitHub accounts with 2FA):**
```bash
git clone https://<USERNAME>:<TOKEN>@github.com/dc4eu/educational-pilot-deployment.git
```

**Option B (for GitHub accounts without 2FA):**
```bash
git clone https://github.com/dc4eu/educational-pilot-deployment.git
```

Then:
```bash
cd educational-pilot-deployment
git checkout v0.0.1
git pull
```

## Docker Configuration

Log into the Docker registry:
```bash
docker login -u dc4eupa -p dc4eupa ossdc4eu.urv.cat:8081
```

Ensure Docker Compose is configured to use the `.env` file and the appropriate YAML descriptor:
```bash
docker compose --env-file ./.env up
```

## Environment and Deployment Files

Before deployment, make sure to configure the following files:

- `.env`
- `docker-compose.yml` or `docker-compose-ownReverseProxy.yml`

Detailed configuration instructions are provided in these guides:
- [Environment File Configuration](./environment-config.md)
- [HTTPS Support Configuration](./https-support.md)

## Deployment and Verification

To start the environment:
```bash
docker compose --env-file ./.env up
```

**Service endpoints examples (with HTTPS):**
- Issuer GUI: `https://uself-issuer-gui.lsp[ORG].domain`
- PID Generator: `https://uself-pid-generator.lsp[ORG].domain`
- Verifier GUI: `https://uself-verifier-gui.lsp[ORG].domain`

Check logs and browser availability to confirm successful deployment.

---

For troubleshooting, see the [Annex and Troubleshooting Guide](./troubleshooting.md).

---

**© 2023-2025 DC4EU** – Co-funded by the European Union's Digital Europe Programme under Grant Agreement no. 101102611

