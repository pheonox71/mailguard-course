// Demo entrypoint for the local worker image.
// Implement worker.ParseQueueMessage / ShouldDLQ first, then wire QUEUE_URL
// (LocalStack or ElasticMQ) in your lab compose.
package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("mailguard-worker image: implement package worker, then connect QUEUE_URL.")
	fmt.Println("See starter/docker-compose.queue.yml and Module 09 readings.")
	if len(os.Args) > 1 && os.Args[1] == "--help" {
		os.Exit(0)
	}
}
