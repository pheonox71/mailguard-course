// Demo entrypoint for the local worker image.
// Implement worker.ParseQueueMessage / ShouldDLQ first, then wire QUEUE_URL
// to ElasticMQ (starter/docker-compose.queue.yml — course default) or cloud SQS.
// When using AWS, import AWS SDK for Go v2 only (not aws-sdk-go v1).
// Visibility timeout is a lease; map ApproximateReceiveCount → attempt for DLQ.
package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("mailguard-worker image: implement package worker, then connect QUEUE_URL.")
	fmt.Println("Default local broker: ElasticMQ (starter/docker-compose.queue.yml).")
	fmt.Println("See Module 09 readings for lease / ApproximateReceiveCount / SDK Go v2.")
	if len(os.Args) > 1 && os.Args[1] == "--help" {
		os.Exit(0)
	}
}
