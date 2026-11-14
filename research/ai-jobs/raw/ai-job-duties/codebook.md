# Codebook: what the hire actually does

This is the instruction used to label `labels.csv`. Each posting came with an `id`, the job family it was filed under and the responsibilities part of the posting text (sometimes the start of the full text, sometimes in German or another language, sometimes with HTML left in).

For every posting, record which duties the posting explicitly assigns to the person being hired. Code only what the text says the hire will do. Company descriptions, product blurbs ("our AI-powered platform…"), benefits and requirement lists (skills, experience) are no duties; ignore them unless phrased as something the hire will do. Multi-label: assign every code that applies, or none.

## Codes

- `CORE`: does the classic work of this job family itself (marketing: runs campaigns, content, channels, positioning; product: owns roadmap, discovery, specs, launches; sales and CS: manages accounts, closes deals, pipeline; governance, legal, risk: audits, compliance reviews, contracts, risk assessments; operations: runs and improves business processes; transformation and strategy: business strategy or organisational change work).
- `AI_BUILD`: personally builds AI or automation: agents, prompts and prompt libraries, LLM workflows, automations (no-code tools like Zapier or n8n included), pipelines, internal AI tools, models.
- `AI_USE`: is expected to use AI tools in their own daily work ("leverage AI tools to speed up content", "use ChatGPT or Claude for analysis") without building systems for others.
- `AI_ROLLOUT`: drives adoption of AI or automation across teams or processes: implementation, change management, deployment into workflows, integration of AI into how the organisation works.
- `AI_TRAIN`: trains, upskills, coaches or enables other people on AI; writes playbooks and guidelines, runs office hours or champion networks.
- `AI_STRATEGY`: defines AI strategy or roadmap, finds and ranks AI use cases or opportunities.
- `AI_MEASURE`: defines metrics or measures the impact, ROI or value of AI work.
- `AI_VENDOR`: evaluates, selects or manages AI tools, vendors, platforms or partners.
- `AI_GOVERN`: AI policy, AI risk, AI compliance, responsible or ethical AI, guardrails, AI regulation (EU AI Act and others).
- `AI_PRODUCT`: the job is about an AI product or feature the company sells or builds for customers (marketing, selling, managing, designing or supporting an AI product), as opposed to using AI inside the company.
- `CUSTOMER`: works directly with external customers or clients (selling, advising, implementing, onboarding, consulting, support).
- `LEAD`: manages a team of people (direct reports) or builds a team.

## Extra fields

- `ai_share`: how much of the listed duties are about AI (any AI code, or AI as the subject of the work): `0` (nothing), `low` (under a quarter), `mid` (a quarter to three quarters), `high` (over three quarters). In `labels.csv` the value `0` is written as `none`.
- `core`: 3 to 8 plain English words on what this person mainly does all day. In `labels.csv` this is `main_duty`.
- `quality`: `ok` if the text contains real duties; `boiler` if it is mostly navigation, cookie banner, JSON or company blurb with no duties (then nothing else is coded and `ai_share` is `0`). In `labels.csv` these are `duties_found` and `no_duties_in_text`.

## Rules

Be consistent and literal. Do not guess duties that are not written. Do not skip lines. When unsure between two codes, include both only if the text supports both.

## Version 1.1 clarifications (22 October 2026)

An independent audit found that the codebook allowed two readings of a few codes. These rules close them. `AI_PRODUCT`, `AI_ROLLOUT`, `CUSTOMER`, `AI_MEASURE` and `AI_STRATEGY` were re-labelled for every posting under version 1.1. The other codes come from the version 1.0 labelling.

1. **AI_PRODUCT vs bespoke client work.** Code AI_PRODUCT only when the posting names or clearly describes a product or feature the employer itself sells or ships to its own customers or end users. Bespoke AI solutions a consultancy or agency builds for a client are not AI_PRODUCT. Deploying the employer's own AI product at a customer site is AI_PRODUCT plus CUSTOMER. An AI tool built for the employer's own staff is not AI_PRODUCT.
2. **AI_BUILD vs AI_ROLLOUT for a builder who also deploys.** A hire who builds a solution and ships it is AI_BUILD. Add AI_ROLLOUT only when the text assigns adoption work beyond shipping: driving usage across teams, change management, embedding into existing processes, champion networks, scaling a pilot to other units. A consultant who leads implementation and adoption of AI at a client is AI_ROLLOUT.
3. **CUSTOMER: discovery and partners.** CUSTOMER means a commercial or delivery relationship with external customers or clients. Customer interviews and user research for product discovery are not CUSTOMER. Channel partners, suppliers and supply-side contractors are not customers unless the text calls them customers or clients; a wholesale buyer of the employer's goods is a customer.
4. **Automation without AI.** Automation counts toward AI_BUILD or AI_ROLLOUT only when the text names AI, an AI tool or an agent, or the automation runs on an AI or no-code/RPA automation platform. CRM workflow configuration and "identify automation opportunities" with no AI mentioned get no AI code.
5. **Title-only AI.** A title or company description that mentions AI does not make the duties AI-related. When the duty list contains nothing about AI, no AI code applies and ai_share is 0.
6. **AI_MEASURE vs AI_STRATEGY.** AI_MEASURE covers metrics, tracking or reporting of the impact of AI in use or being rolled out (hours saved, ROI realised, adoption, quality of AI output in use). Pre-build feasibility or ROI estimates belong to AI_STRATEGY. Product KPIs of an AI feature are not AI_MEASURE unless the text names AI impact measurement as a separate duty.
7. **AI_STRATEGY vs AI product management.** AI_STRATEGY means deciding where and how AI should be applied: an AI strategy or AI roadmap for the organisation, a unit or a client; finding, assessing and prioritising AI use cases; choosing which AI models or technologies to adopt. Owning the vision, roadmap, backlog or go-to-market of the employer's AI product is AI_PRODUCT, not AI_STRATEGY.
