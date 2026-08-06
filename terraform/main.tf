# Definimos el recurso del clúster de Kind
resource "kind_cluster" "pihole_cluster" {
  name           = "pihole-lab"
  node_image     = "kindest/node:v1.31.0"
  wait_for_ready = true

  kind_config {
    kind        = "Cluster"
    api_version = "kind.x-k8s.io/v1alpha4"
    node {
      role = "control-plane"

      kubeadm_config_patches = [
        "kind: InitConfiguration\nnodeRegistration:\n  kubeadmNodeAnnotations:\n    ingress-ready: \"true\"\n"
      ]
      extra_port_mappings {
        container_port = 80
        host_port      = 80
        protocol       = "TCP"
      }

      extra_port_mappings {
        container_port = 443
        host_port      = 443
        protocol       = "TCP"
      }
    }
    node {
      role = "worker"
    }
  }
}
