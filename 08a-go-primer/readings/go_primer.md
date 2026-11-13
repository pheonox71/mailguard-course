# Go primer

**Why this matters.** Module 09’s worker consumes queue messages and applies hold/allow/reject. **Go** fits small, explicit network services: fast compile, static binaries, and straightforward concurrency — useful when a Python API owns HTTP and a worker owns async decisions. You *could* keep everything in one Python process; splitting a worker is how teams isolate retries, DLQs, and deploy cadence without blocking the API.

**How it works.** You install the toolchain, write packages under a module (`go.mod`), and verify behavior with `go test`. Interfaces describe ports (e.g. a queue) so the kata can stay in-memory before cloud SQS. On the job, the same pattern shows up in email and identity pipelines: thin consumers, table-driven tests, swap local fakes for cloud queues later.

This primer has no assignment, quiz, or download pack.

---

## What Go is

**Go** is an open-source language from Google, common for CLIs, proxies, and cloud workers.

## Why industry uses it

Ops-friendly deploy (single binary), good standard library for HTTP/JSON, and predictable performance for queue consumers. Many security and platform teams keep Go beside Python services.

## Key concepts for Module 09

| Concept | Why you care |
|---------|----------------|
| `go.mod` / packages | Reproducible module layout |
| exported names (`TitleCase`) | Public API of your worker package |
| interfaces | Swap in-memory queue for SQS later |
| `go test ./...` | Same red/green loop as pytest |

## Install and run

1. [Go install docs](https://go.dev/doc/install)
2. Check: `go version`

```bash
# Why: scratch module outside the course repo
mkdir -p /tmp/mg-go-primer && cd /tmp/mg-go-primer
# Why: go.mod pins the module path so imports and `go test` resolve
go mod init example.com/mgprimer
```

## Tiny hands-on example

```bash
cat > /tmp/mg-go-primer/decision.go << 'EOF'
package primer

// Decision is a MailGuard-style outcome.
func Decision(score int) string {
        // Why: tiny pure function — easy to unit test in Module 09
        if score >= 80 {
                return "hold"
        }
        return "allow"
}
EOF
cat > /tmp/mg-go-primer/decision_test.go << 'EOF'
package primer

import "testing"

func TestDecision(t *testing.T) {
        if Decision(90) != "hold" {
                t.Fatalf("expected hold")
        }
}
EOF
cd /tmp/mg-go-primer && go test ./...
```

**How:** Production code + `_test.go` live side by side; `go test` compiles and runs them — Module 09 uses the same pattern.

## Official docs

1. [Go install](https://go.dev/doc/install)
2. [A Tour of Go](https://go.dev/tour/)
3. [go test docs](https://pkg.go.dev/testing)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`09-mailguard-worker`).

This primer has **no** assignment, quiz, or download pack.
