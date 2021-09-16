#! /bin/bash
# exit script when any command ran here returns with non-zero exit code
set -e

COMMIT_SHA1=$COMMIT_HASH

# We must export it so it's available for envsubst
export COMMIT_SHA1=$COMMIT_SHA1

if [ $CODEBUILD_WEBHOOK_TRIGGER == 'branch/staging' ]; then
    DEPLOY_BRANCH=stage
    KUBERNETES_SERVER=$STAGE_KUBERNETES_SERVER
    KUBERNETES_TOKEN=$STAGE_KUBERNETES_TOKEN
elif [ $CODEBUILD_WEBHOOK_TRIGGER == 'branch/dev' ]; then
    DEPLOY_BRANCH=dev
    KUBERNETES_SERVER=$DEV_KUBERNETES_SERVER
    KUBERNETES_TOKEN=$DEV_KUBERNETES_TOKEN    
else
    echo "Not on a deployable branch!"
fi
# since the only way for envsubst to work on files is using input/output redirection,
#  it's not possible to do in-place substitution, so we need to save the output to another file
#  and overwrite the original with that one.
if [ "$DEPLOY_BRANCH" ]; then
    envsubst <./kube/$DEPLOY_BRANCH/docs-deployment.yml >./kube/$DEPLOY_BRANCH/docs-deployment.yml.out
    mv ./kube/$DEPLOY_BRANCH/docs-deployment.yml.out ./kube/$DEPLOY_BRANCH/docs-deployment.yml

    ./kubectl \
    --kubeconfig=/dev/null \
    --server=$KUBERNETES_SERVER \
    --token=$KUBERNETES_TOKEN \
    --insecure-skip-tls-verify=true \
    apply -f ./kube/$DEPLOY_BRANCH/
else
    echo "DEPLOY_BRANCH is empty, not running."
fi
