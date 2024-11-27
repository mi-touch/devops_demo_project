terraform {
    required_providers {
      minikube = {
        source = "scott-the-programmer/minikube"
        version = "0.4.2"
      }
    } 
}

provider "minikube" {
    kubernetes_version = "v1.30.0"
}

resource "minikube_cluster" "minikube_docker" {
    driver = "docker"
    cluster_name = "complete-devops-project"
    kubernetes_version = "v1.30.0"
    cpus = 2
    memory = 2048
    addons = [
      "default-storageclass",
      "storage-provisioner"
    ]
}

# resource "minikube_cluster" "minikube_docker" {
#   driver       = "docker"
#   cluster_name = "complete-devops-project"
#   cpus         = 2
#   memory       = 2048

#   addons = []
# }
