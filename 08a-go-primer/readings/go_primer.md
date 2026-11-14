# Go primer

**Why this matters.** Module 09’s worker consumes queue messages and applies hold/allow/reject. **Go** fits small, explicit network services: fast compile, static binaries, and straightforward concurrency — useful when a Python API owns HTTP and a worker owns async decisions. You *could* keep everything in one Python process; splitting a worker is how teams isolate retries, DLQs, and deploy cadence without blocking the API.

**How it works.**

1. Install the Go toolchain and confirm with `go version`.
2. Create a module (`go mod init`) so imports and tests resolve.
3. Write packages with exported (`TitleCase`) names for the worker’s public surface.
4. Describe ports with **interfaces** (e.g. a queue) so the kata stays in-memory before cloud SQS.
5. Verify with `go test ./...` — table-driven tests lock decisions the same way pytest does for the API.
6. On the job, the same pattern shows up in email and identity pipelines: thin consumers, table-driven tests, swap local fakes for cloud queues later.

### Worked example

Tiny decision function + test (same shape Module 09 uses):

```go
package primer

func Decision(score int) string {
        // Why: tiny pure function — easy to unit test in Module 09
        if score >= 80 {
                return "hold"
        }
        return "allow"
}
```

```go
func TestDecision(t *testing.T) {
        if Decision(90) != "hold" {
                t.Fatalf("expected hold")
        }
}
```

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

### Common misconceptions / what goes wrong

- **“Go replaces the Python API.”** The split is intentional: HTTP/policy in one process, async side effects in another — shared JSON vocabulary, not a rewrite.
- **“Call the cloud SDK from every package.”** Interfaces keep LocalStack/in-memory fakes testable; sprinkle SDK calls and unit tests need the network.
- **“Tests are optional until SQS.”** Table-driven `go test` locks the decision contract before any broker exists.


## Videos (verified)

1. **[Learn Go Programming - Golang Tutorial for Beginners](https://www.youtube.com/watch?v=YS4e4q9oBaU)**  
   Why it helps: Go toolchain before the worker module.

## Official docs

1. [Go install](https://go.dev/doc/install)
2. [A Tour of Go](https://go.dev/tour/)
3. [go test docs](https://pkg.go.dev/testing)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`09-mailguard-worker`).

This primer has **no** assignment, quiz, or download pack.
