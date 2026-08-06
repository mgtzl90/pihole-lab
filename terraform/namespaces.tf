resource "kubernetes_namespace" "argocd" {
  metadata {
    name = "argocd"
  }
}

resource "kubernetes_namespace" "pihole" {
  metadata {
    name = "pihole"
  }
}
