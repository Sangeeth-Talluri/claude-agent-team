# Next Steps — decisions only the owner can make

The scaffold is done. These three answers unblock Phase 1 (see Plan 2 §11):

## 1. Where will the bots live?
- [ ] An always-on machine at home (routines run 24/7, Slack Socket Mode is easy)
- [ ] A small cloud VM (always on, better for Slack webhooks, small monthly cost)
- [ ] Your laptop (simplest, but routines only run while it is awake)

## 2. What does Project Bot — Main own?
- [ ] Repo: ______________________ (one repo, with tests in CI is ideal)
- [ ] Its feedback channel: ______________________ (Slack channel, GitHub Issues, or email)
- [ ] Does that repo already have `CLAUDE.md` + a verification skill?
      If not, Plan 1 Phases 1–2 come first for that repo.

## 3. Which Slack, if any?
- [ ] A workspace where you can add an app (needed for the feedback-watch routine)
- [ ] No Slack for v1 — use GitHub Issues / email as the signal source instead

## Then, in order
1. Fill every `TODO(owner)` in the folder (search for the string).
2. Connect Gmail + Calendar **read-only** for the Chief of Staff and Ops bot.
3. Turn on ONE routine: the Chief of Staff morning brief. Live with it for a few days.
4. Add the project bot's Slack watch. Then the morning launch. Payments (virtual card)
   are Phase 5 — deliberately last.

Nothing in this folder runs, connects, or schedules anything until you say go.
