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

good_pod_level_non_root := {
	"kind": "Deployment",
	"spec": {"template": {"spec": {
		"securityContext": {"runAsNonRoot": true},
		"containers": [{
			"name": "good",
			"image": "good:1.2.3",
			"readinessProbe": {"httpGet": {"path": "/readyz", "port": 8080}},
			"livenessProbe": {"httpGet": {"path": "/livez", "port": 8080}},
		}],
	}}},
}

bad_latest := {
	"kind": "Deployment",
	"spec": {"template": {"spec": {"containers": [{
		"name": "bad",
		"image": "bad:latest",
	}]}}},
}

missing_probes := {
	"kind": "Deployment",
	"spec": {"template": {"spec": {"containers": [{
		"name": "noprobe",
		"image": "app:1.0.0",
		"securityContext": {"runAsNonRoot": true},
	}]}}},
}

missing_non_root := {
	"kind": "Deployment",
	"spec": {"template": {"spec": {"containers": [{
		"name": "rooty",
		"image": "app:1.0.0",
		"readinessProbe": {"httpGet": {"path": "/readyz", "port": 8080}},
		"livenessProbe": {"httpGet": {"path": "/livez", "port": 8080}},
	}]}}},
}

test_good_allows if {
	count(main.deny) == 0 with input as good_deployment
}

test_pod_level_non_root_allows if {
	count(main.deny) == 0 with input as good_pod_level_non_root
}

test_latest_denied if {
	some msg in main.deny with input as bad_latest
	contains(msg, ":latest")
}

test_missing_probe_denied if {
	some msg in main.deny with input as missing_probes
	contains(msg, "readinessProbe")
}

test_missing_non_root_denied if {
	some msg in main.deny with input as missing_non_root
	contains(msg, "runAsNonRoot")
}
