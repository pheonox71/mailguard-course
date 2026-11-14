package main_test

import rego.v1

import data.main

good_deployment := {
	"kind": "Deployment",
	"spec": {"template": {"spec": {"containers": [{
		"name": "good",
		"image": "good:1.2.3",
		"securityContext": {"runAsNonRoot": true},
		"readinessProbe": {"httpGet": {"path": "/healthz", "port": 8080}},
		"livenessProbe": {"httpGet": {"path": "/healthz", "port": 8080}},
	}]}}},
}

bad_latest := {
	"kind": "Deployment",
	"spec": {"template": {"spec": {"containers": [{
		"name": "bad",
		"image": "bad:latest",
	}]}}},
}

test_good_allows if {
	count(main.deny) == 0 with input as good_deployment
}

test_latest_denied if {
	some msg in main.deny with input as bad_latest
	contains(msg, ":latest")
}
