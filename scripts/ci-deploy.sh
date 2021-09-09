#! /bin/bash
# exit script when any command ran here returns with non-zero exit code
set -e

COMMIT_SHA1=$COMMIT_HASH

# We must export it so it's available for envsubst
export COMMIT_SHA1=$COMMIT_SHA1

# since the only way for envsubst to work on files is using input/output redirection,
#  it's not possible to do in-place substitution, so we need to save the output to another file
#  and overwrite the original with that one.

envsubst <./kube/stage/docs-deployment.yml >./kube/stage/docs-deployment.yml.out
mv ./kube/stage/docs-deployment.yml.out ./kube/stage/docs-deployment.yml

./kubectl \
--kubeconfig=/dev/null \
--server=$KUBERNETES_SERVER \
--token=$KUBERNETES_TOKEN \
--insecure-skip-tls-verify=true \
apply -f ./kube/stage/