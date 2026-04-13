# GitHub Intelligence Brief — AetherAI
**Source:** GitHub Trending · Week of April 10, 2026
**Prepared for:** AetherAI platform (hsharmagxi-debug/aetherAI)
**Current stack:** Docker Compose · Ollama · ChromaDB · Automatic1111 · Open WebUI · AI Gateway

---

## Executive Summary

Five repos from this week directly extend or enhance the AetherAI stack.
Two are drop-in Docker Compose additions. One adds voice. One adds mobile.
One provides architectural patterns for multi-LLM routing.
Together they fill the gaps between AetherAI's current capabilities
and a production-grade self-hosted AI platform.

---

## 1. onyx-dot-app/onyx → Intelligence & RAG Layer
**★ 26.5k | +5,556 this week | Python + TypeScript | MIT CE**

### Why It Matters
Onyx is what AetherAI's knowledge layer should become.
It natively supports Ollama as an LLM backend — meaning it sits
directly on top of your existing stack. It adds agentic RAG,
50+ connectors, Deep Research, and enterprise access control
without replacing anything you've already built.

### Integration Path with AetherAI
Onyx supports Ollama natively via LiteLLM. Point Onyx at
`http://ollama:11434` and it uses your existing local models.

### What Onyx Adds to AetherAI
- Agentic RAG on top of ChromaDB-style hybrid search
- 50+ data source connectors (Slack, Notion, GitHub, web crawler)
- Deep Research: multi-step investigation (#1 open leaderboard, Feb 2026)
- Sandboxed Python code execution for data analysis
- Voice (TTS/STT) + Vision + Image generation
- SSO (OIDC, SAML), RBAC, audit logs, whitelabeling (Enterprise EE)
- MCP integration — Atlas/Hermes can call Onyx as a tool

### Implementation Guide
```yaml
# Add to docker-compose.yml:
  onyx-backend:
    image: onyxdotapp/onyx-backend:latest
    environment:
      - GEN_AI_MODEL_PROVIDER=ollama
      - GEN_AI_MODEL_VERSION=llama3.2
      - OLLAMA_BASE_URL=http://ollama:11434
      - VESPA_DEPLOYMENT_ZIP=...
    depends_on:
      - ollama
      - postgres
    ports:
      - "8080:8080"

  onyx-frontend:
    image: onyxdotapp/onyx-web-server:latest
    ports:
      - "3000:3000"
```
Full Compose reference: github.com/onyx-dot-app/onyx/blob/main/deployment/docker_compose/

---

## 2. NousResearch/hermes-agent → Persistent Agent Daemon
**★ 54.3k | +19,765 this week | Python | MIT**

### Why It Matters
Hermes is a self-improving agent that runs on Docker, connects to any
LLM via custom endpoint, and extends via MCP. Add it to AetherAI as
a persistent background agent that handles scheduled tasks, automation,
and cross-session memory — filling the gap between Open WebUI's chat
interface and true agentic capability.

### What Hermes Adds to AetherAI
- Persistent cross-session memory (FTS5 + LLM summarization)
- Closed learning loop: task → extract skill → improve next run
- 40+ built-in tools, MCP extensible
- Scheduled automation (cron): auto-run reports, backups, audits
- Cross-platform: CLI, Telegram, Discord, Slack, WhatsApp interfaces
- Runs on Docker natively — no extra infrastructure needed

### Integration with AetherAI
Hermes connects to Ollama via OpenAI-compatible custom endpoint:
```bash
# In hermes config, set:
OPENAI_API_BASE=http://ollama:11434/v1
OPENAI_API_KEY=ollama  # dummy key
MODEL=llama3.2         # or any model loaded in Ollama
```

### Implementation Guide
```bash
# Install Hermes on your AetherAI host:
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Or add to docker-compose.yml:
  hermes:
    image: nousresearch/hermes-agent:latest
    environment:
      - OPENAI_API_BASE=http://ollama:11434/v1
      - MODEL=llama3.2
    volumes:
      - hermes-memory:/root/.hermes
    depends_on:
      - ollama
```
Then: `hermes gateway` to enable Telegram/Slack interfaces.

---

## 3. NVIDIA/personaplex → Voice Interface Layer
**★ 8.9k | +2,745 this week | Python | MIT code + NVIDIA Open Model weights**

### Why It Matters
AetherAI has no voice interface. PersonaPlex adds real-time, full-duplex
speech with controllable personas. It runs locally (GPU required),
uses your choice of persona via text prompt, and supports 16 voice options.
Add it as a voice gateway service in docker-compose.yml.

### What PersonaPlex Adds to AetherAI
- Full-duplex speech: model listens and talks simultaneously
- 16 pre-packaged voice embeddings (8 female, 8 male)
- Persona control via text prompt: teacher, assistant, customer service, casual
- Connects to any LLM backbone (uses Helium by default, swappable)
- Web UI at localhost:8998 out of the box

### Implementation Guide
```bash
# Prerequisites:
pip install moshi torch --index-url https://download.pytorch.org/whl/cu130
sudo apt-get install libopus-dev

# Download weights from HuggingFace:
huggingface-cli download nvidia/personaplex

# Launch voice server:
python -m moshi.server --ssl "$SSL_DIR"
# Access at https://localhost:8998
```

**Docker Compose addition:**
```yaml
  personaplex:
    image: nvidia/personaplex:latest
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
    ports:
      - "8998:8998"
    volumes:
      - personaplex-models:/models
```

**Use CPU offload if GPU memory is limited:**
```bash
python -m moshi.server --ssl "$SSL_DIR" --cpu-offload
```

---

## 4. google-ai-edge/gallery → Mobile Companion App
**★ 20.1k | +4,326 this week | Kotlin**

### Why It Matters
Google Gallery is the reference mobile app for on-device LLMs (Gemma 4).
It supports Android 12+ and iOS 17+, runs 100% offline, and includes
function calling that can route to external APIs — including AetherAI's
gateway. Use it as AetherAI's privacy-first mobile front-end: lightweight
tasks on device, heavy inference routed to the AetherAI Docker stack.

### What It Adds to AetherAI
- On-device chat, image analysis, audio transcription
- Agent Skills: on-device function calling with Wikipedia, Maps tools
- Route heavier requests to AetherAI gateway via network call
- 100% private mobile experience — data stays on device unless routed

### Implementation Guide
1. Install Google Gallery from Play Store / App Store / GitHub APK.
2. In Gallery's "Agent Skills" configuration, add AetherAI gateway
   as a custom tool endpoint:
   ```json
   {
     "name": "aetherAI",
     "endpoint": "http://your-aetherAI-host:port/v1/chat/completions",
     "description": "Route to local AetherAI for heavy inference"
   }
   ```
3. Use Gallery for: quick queries, image analysis, voice transcription.
4. Route to AetherAI for: Automatic1111 generation, deep research, RAG.

---

## 5. HKUDS/DeepTutor → Multi-LLM Routing Pattern
**★ 15.7k | +3,233 this week | Python | MIT**

### Why It Matters
DeepTutor supports 25+ LLM providers with seamless mode escalation.
Its routing architecture (CLI → web UI → Docker, same session context)
is a clean reference for AetherAI's multi-model routing layer —
deciding which task goes to which model (Ollama local vs. API fallback).

### What to Borrow
- Multi-provider routing pattern: local-first, API fallback
- Session context persistence across model switches
- Mode-based task routing: simple tasks → small model, complex → large
- Docker deployment patterns for multi-service Python AI stacks

---

## AetherAI Enhanced Stack (After Implementation)

```
┌─────────────────────────────────────────────────┐
│  Mobile: Google Gallery (on-device, Gemma 4)    │
├─────────────────────────────────────────────────┤
│  Voice: PersonaPlex (full-duplex, personas)     │
├─────────────────────────────────────────────────┤
│  Agent: Hermes (persistent memory, 40+ tools)   │
├─────────────────────────────────────────────────┤
│  Intelligence: Onyx (RAG, connectors, research) │
├─────────────────────────────────────────────────┤
│  EXISTING: Open WebUI · Ollama · ChromaDB       │
│            Automatic1111 · AI Gateway           │
└─────────────────────────────────────────────────┘
```

## Priority Order

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| P0 | Add Onyx CE to docker-compose.yml (Ollama backend) | 1 day | Very High |
| P1 | Add Hermes agent daemon to docker-compose.yml | 4 hours | High |
| P2 | Add PersonaPlex voice service | 1 day | High |
| P3 | Configure Google Gallery → AetherAI gateway routing | 2 hours | Medium |
| P4 | Study DeepTutor routing for multi-model architecture | Reference only | Medium |
