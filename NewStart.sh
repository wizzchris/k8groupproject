eval $(minikube docker-env)
docker build -t codebreaker -f Dockerfile/AppDockerfile .
kbuild # kustomize build | kubectl apply -f -
