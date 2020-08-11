eval $(minikube docker-env)
docker build . -t codebreaker
minikube addons enable ingress
kubectl create -f kustomiz.yaml
minikube service app --url
