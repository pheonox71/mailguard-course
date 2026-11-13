# Reading — MailGuard Worker

## Learning objectives

1. Consume queued messages and apply rule decisions.
2. Keep a queue interface so local demos and cloud queues share code.
3. Document the contract with the Python API.

## Short intro

API services accept operator input; **workers** apply decisions asynchronously — hold persistence, notifications, or release to an MTA. This module is a Go worker with an in-memory queue interface and table-driven tests.

## Read these (verified)

1. [Go — Getting Started](https://go.dev/doc/tutorial/getting-started)
2. [Go — testing package](https://pkg.go.dev/testing)
3. [AWS SQS — How it works](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) (conceptual; use a local interface first)

## Next step

Continue with the assignment from the downloads on this page.
