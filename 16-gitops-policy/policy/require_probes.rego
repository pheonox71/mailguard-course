# Conftest / OPA policy (Rego v1): Deployments must declare readiness + liveness
# probes, must not use the :latest tag, and must set runAsNonRoot effectively
# true for every container. Container securityContext.runAsNonRoot wins when
# set (including explicit false); inherit the pod value only when the container
# leaves the field unset.
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

container_sets_run_as_non_root(container) if {
	object.get(object.get(container, "securityContext", {}), "runAsNonRoot", null) != null
}

# Explicit container true → effective true.
effective_run_as_non_root(container) if {
	container_sets_run_as_non_root(container)
	container.securityContext.runAsNonRoot == true
}

# Unset on container → inherit pod true only.
effective_run_as_non_root(container) if {
	not container_sets_run_as_non_root(container)
	input.spec.template.spec.securityContext.runAsNonRoot == true
}

deny contains msg if {
	input.kind == "Deployment"
	some container in input.spec.template.spec.containers
	not effective_run_as_non_root(container)
	msg := sprintf(
		"container %q must run as non-root (set securityContext.runAsNonRoot true, or leave it unset and set it on the pod; explicit false is denied)",
		[container.name],
	)
}
