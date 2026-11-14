# Conftest / OPA policy (Rego v1): Deployments must declare readiness + liveness
# probes, must not use the :latest tag, and containers must set runAsNonRoot.
package main

import rego.v1

deny contains msg if {
	input.kind == "Deployment"
	some container in input.spec.template.spec.containers
	not container.readinessProbe
	msg := sprintf("container %q missing readinessProbe", [container.name])
}

deny contains msg if {
	input.kind == "Deployment"
	some container in input.spec.template.spec.containers
	not container.livenessProbe
	msg := sprintf("container %q missing livenessProbe", [container.name])
}

deny contains msg if {
	input.kind == "Deployment"
	some container in input.spec.template.spec.containers
	endswith(container.image, ":latest")
	msg := sprintf("container %q uses :latest tag", [container.name])
}

deny contains msg if {
	input.kind == "Deployment"
	some container in input.spec.template.spec.containers
	not container.securityContext.runAsNonRoot
	msg := sprintf("container %q must set securityContext.runAsNonRoot", [container.name])
}
