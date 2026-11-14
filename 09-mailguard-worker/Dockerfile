# Local/demo image for the MailGuard worker.
# Build from this module directory (after implementing package worker if you want tests in CI):
#   docker build -t mailguard-worker:local .
FROM golang:1.22-alpine AS build
WORKDIR /src
COPY go.mod ./
COPY worker ./worker
COPY cmd ./cmd
RUN CGO_ENABLED=0 go build -o /out/worker ./cmd/worker

FROM alpine:3.20
WORKDIR /app
COPY --from=build /out/worker /app/worker
CMD ["/app/worker"]
