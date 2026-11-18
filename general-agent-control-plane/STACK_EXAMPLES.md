# Stack Examples — filling in verify.config.yaml

The verify skill reads `.claude/skills/verify/verify.config.yaml`: under `checks:`,
one `name: command` line per check. The command runs in the repo root and its exit
code is the verdict. Copy the block for your stack, adjust the TODOs, and delete
the checks your repo does not have — an absent check reports NOT CONFIGURED, which
is honest; a fake check that always exits 0 is not.

Whichever stack: `smoke` should prove the built thing actually runs — start it (or
hit a locally running instance) and assert a real response, not just "it compiled".

## Node / TypeScript (npm — swap in pnpm/yarn/bun equivalents)
```yaml
checks:
  tests: npm test
  lint: npm run lint
  typecheck: npx tsc --noEmit
  build: npm run build
  smoke: TODO(owner) e.g. npm run start & sleep 3 && curl -sf http://localhost:3000/ ; kill %1
```
Notes: if tests live in a separate script (`test:unit`, `test:e2e`), name checks
after them — `tests: npm run test:unit` plus an extra line `e2e: npm run test:e2e`.
Extra check worth adding: `audit: npm audit --audit-level=high` (fails on known
high-severity dependency vulnerabilities).

## Python
```yaml
checks:
  tests: pytest -q
  lint: ruff check .
  typecheck: mypy .
  build: python -m build
  smoke: TODO(owner) e.g. python -c "import <your_package>" or start the app and curl its health route
```
Notes: no build step (scripts, internal tools)? Delete `build` or point it at
`python -m compileall .`. Using `uv`? Prefix commands with `uv run` so they run in
the project environment.

## Go
```yaml
checks:
  tests: go test ./...
  lint: go vet ./...
  typecheck: go build ./...
  build: go build ./...
  smoke: TODO(owner) e.g. go run . --help or start the binary and curl its health endpoint
```
Notes: `golangci-lint run` is a stronger `lint` if the repo already uses it.
Add `race: go test -race ./...` as its own check for concurrent code.

## Java (Maven — Gradle equivalents in comments)
```yaml
checks:
  tests: ./mvnw -q test
  lint: ./mvnw -q checkstyle:check
  typecheck: ./mvnw -q compile
  build: ./mvnw -q package -DskipTests
  smoke: TODO(owner) e.g. start the jar and curl its health/actuator endpoint
```
Notes: Gradle: `./gradlew test`, `./gradlew checkstyleMain`, `./gradlew assemble`.
If the repo has no checkstyle/spotless setup, drop `lint` rather than inventing one
in the agent kit — propose it as its own PR instead.

## Rust
```yaml
checks:
  tests: cargo test
  lint: cargo clippy -- -D warnings
  typecheck: cargo check
  build: cargo build --release
  smoke: TODO(owner) e.g. ./target/release/<binary> --version
```
Notes: add `fmt: cargo fmt --check` as its own check if formatting is enforced.

## Mixed / monorepo
One check can fan out: `tests: npm test && (cd services/api && go test ./...)`.
Better: define per-area checks (`tests-web:`, `tests-api:`) so a failure names its
area in the evidence bundle, and let `verify.py all` run the set.
