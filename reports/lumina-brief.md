# GitHub Intelligence Brief — Lumina Numerology
**Source:** GitHub Trending · Week of April 10, 2026
**Prepared for:** Lumina Numerology product team

---

## Executive Summary

Four repos from this week's trending data are applicable to Lumina.
They cover: voice-based readings, cross-platform user continuity,
personalized journey UX, and on-device privacy for sensitive data.
Together they map out a clear product evolution from a static
numerology tool to a living, conversational, cross-platform companion.

---

## 1. NVIDIA/personaplex → Voice Numerology Readings
**★ 8.9k | +2,745 this week | Python | MIT code + NVIDIA Open Model weights**

### Why It Matters
Numerology is inherently personal and ceremonial. Text-based output
misses the gravitas of the reading experience. PersonaPlex enables
real-time, full-duplex voice with controllable personas — a "mystic guide"
persona reading your life path feels fundamentally different from
reading it on a screen. This is a product differentiator no competitor
has shipped.

### What It Enables for Lumina
- **Voice persona system:** define a "Lumina Guide" persona via text prompt.
  The model delivers readings in that voice and personality consistently.
- **Full-duplex conversation:** user asks follow-up questions mid-reading.
  The guide responds naturally, like a real practitioner.
- **16 pre-packaged voices:** choose the voice profile that best fits
  Lumina's brand identity (warm, measured, resonant).
- **Offline capable:** sensitive personal data (birth dates, names)
  never leaves the device during inference.

### Persona Prompt Example
```
You are Lumina, a wise and grounded numerology guide. You speak with
warmth and clarity. You deliver numerological insights with confidence
but invite the user to reflect rather than prescribe. Your tone is
calm, measured, and never rushed.
```

### Implementation Guide
1. Deploy PersonaPlex locally (GPU) or on a private server.
2. Define the "Lumina Guide" persona prompt and select a voice embedding
   (recommend NATF2 or VARF1 for warmth).
3. Build a reading flow: user inputs birth date → backend calculates
   life path, destiny, soul urge numbers → PersonaPlex reads the
   interpretation aloud.
4. Enable follow-up Q&A: full-duplex means user interrupts naturally.
5. Privacy: run inference locally or on a private server — no data
   to third-party APIs.

```bash
# Launch PersonaPlex with Lumina persona:
python -m moshi.server --ssl "$SSL_DIR" \
  --voice-embedding NATF2 \
  --role-prompt "You are Lumina, a wise numerology guide..."
```

---

## 2. NousResearch/hermes-agent → Cross-Platform User Continuity
**★ 54.3k | +19,765 this week | Python | MIT**

### Why It Matters
Most numerology apps are a one-time interaction. Hermes's architecture
proves that persistent cross-session memory is buildable — and users
stay engaged when the system remembers them. Lumina should build a
guide that evolves with the user: remembers their chart, tracks which
numbers they've explored, notices patterns in their questions over time.

### What to Borrow for Lumina
- **Persistent user profile:** store the user's full numerology chart
  (life path, expression, soul urge, personality, destiny numbers)
  in a persistent memory layer. The guide recalls it every session.
- **Cross-platform continuity:** user starts a reading on web, checks
  in via WhatsApp or Telegram, continues seamlessly. Hermes already
  handles this across CLI/Telegram/Discord/Slack/WhatsApp.
- **Closed learning loop:** guide learns which interpretations
  resonate with the user and adjusts future readings accordingly.
- **Scheduled check-ins:** cron-based personal number of the day /
  week messages auto-delivered to the user's preferred platform.

### Implementation Guide
1. Integrate Hermes's memory architecture (FTS5 + LLM summarization)
   as Lumina's user profile backend.
2. At first session: collect birth date, full name → compute full
   chart → store in memory layer.
3. Every subsequent session: load chart from memory, continue
   from where they left off.
4. Enable Telegram/WhatsApp gateway: `hermes gateway` gives users
   a Lumina guide in their existing messaging apps.
5. Set up daily personal number delivery via Hermes cron.

```python
# Lumina user memory schema (stored per user):
{
  "name": "...",
  "birth_date": "...",
  "chart": {
    "life_path": 7,
    "expression": 3,
    "soul_urge": 9,
    "personality": 4,
    "destiny": 11
  },
  "explored_numbers": [7, 3],
  "resonance_notes": "User responds well to career framing of LP7",
  "last_session": "2026-04-10"
}
```

---

## 3. HKUDS/DeepTutor → Personalized Numerology Journey
**★ 15.7k | +3,233 this week | Python | MIT**

### Why It Matters
DeepTutor's "five modes, one thread" model — with persistent personal
TutorBots that evolve with the learner — is the closest public blueprint
for what Lumina's user experience should be: a personalized journey,
not a one-off lookup tool.

### What to Borrow for Lumina
- **Personal TutorBot → Lumina Guide:** persistent entity with memory
  and personality that evolves with the user's numerological exploration.
- **Guided Learning → Guided Numerology Journey:** structured curriculum
  based on the user's chart. "Here are the 5 core numbers in your chart.
  Let's explore them in order of relevance to your current life phase."
- **Mode escalation without losing context:**
  - Level 1: Quick number lookup (Chat mode)
  - Level 2: Deep interpretation with context (Deep Solve)
  - Level 3: Full chart analysis with life phase overlay (Deep Research)
  - Level 4: Interactive quiz — "Test your understanding of your chart"
- **Math Animator equivalent:** "Number Animator" — visualize how a
  user's numbers interact (e.g. life path + personal year cycle = animated
  timeline of energy peaks).

### Implementation Guide
1. Design Lumina's UX as a journey, not a calculator.
   Entry point: "Let's build your chart" → structured 5-step onboarding.
2. After chart is built, present a "Guided Journey" —
   suggested exploration order based on the user's chart configuration.
3. Add knowledge checks: after each number explanation,
   a short reflective prompt ("How does this resonate with your experience?")
4. Store all responses to build a personalized resonance profile
   (feeds back into Hermes's memory layer from #2 above).
5. Build "Number Animator" as a simple canvas animation:
   user's personal year cycle visualized as a 9-year sine wave
   with their current position marked.

---

## 4. google-ai-edge/gallery → On-Device Privacy
**★ 20.1k | +4,326 this week | Kotlin**

### Why It Matters
Numerology requires sensitive personal data: birth date, full name,
sometimes birth time and location. Users are increasingly wary of
sharing this with cloud services. Google Gallery demonstrates that
a fully capable AI experience can run 100% offline on a phone.
Lumina should offer an on-device mode as a trust differentiator.

### What to Borrow for Lumina
- **Offline-first mobile architecture:** all chart calculations and
  core interpretations run on device. No data leaves the phone.
- **Model benchmarking built in:** load custom numerology-tuned
  models (fine-tuned on numerological texts) without app updates.
- **Audio transcription:** user speaks their name/birth date rather
  than typing — reduces friction on mobile.

### Implementation Guide
1. Build Lumina's core calculation engine as a local library
   (no network call required for any numerology math).
2. Bundle a small on-device model (Gemma 2B or similar) for
   basic interpretations — no API key, no signup, instant access.
3. For deeper readings (PersonaPlex voice, Hermes continuity),
   offer opt-in cloud mode with explicit consent.
4. Use Google Gallery's architecture as the reference for the
   Android implementation (Kotlin, on-device function calling).

---

## Lumina Product Roadmap (Derived from This Brief)

### Phase 1 — Privacy Foundation (2 weeks)
- On-device chart calculation (no network required)
- Local interpretation for 5 core numbers
- Data stored locally, encrypted

### Phase 2 — Continuity (4 weeks)
- Persistent user profile (Hermes memory pattern)
- Cross-session chart recall
- Daily personal number push notification

### Phase 3 — Journey UX (6 weeks)
- Guided numerology journey (DeepTutor model)
- Mode escalation: lookup → deep interpretation → full chart
- Knowledge checks and resonance journaling

### Phase 4 — Voice Guide (8 weeks)
- PersonaPlex voice integration
- Lumina Guide persona definition
- Full-duplex reading experience

### Phase 5 — Cross-Platform (10 weeks)
- Telegram / WhatsApp / Discord gateway (Hermes gateway)
- Scheduled check-ins: personal year, monthly, weekly
- Mobile companion (Google Gallery pattern)

---

## Priority Order

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| P0 | On-device chart calculation (no cloud dependency) | 1 week | High |
| P1 | Persistent user profile (Hermes memory pattern) | 1 week | Very High |
| P2 | Guided journey UX (DeepTutor model) | 2 weeks | High |
| P3 | PersonaPlex voice guide | 2 weeks | Differentiator |
| P4 | Cross-platform gateway (Telegram/WhatsApp) | 1 week | High |
