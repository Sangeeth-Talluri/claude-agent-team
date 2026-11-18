# Review Queue

One table (see `schema.sql`), one simple status page on top of it.
Every launched agent writes here; the Chief of Staff's brief is generated from here.
States: queued → planning → implementing → verifying → reviewing → pr-open / done /
failed / needs-human.

Rule from Plan 2 §9: if it is not in the queue, it did not happen — bots never report
work from memory or chat alone.
