disable_mlock = true

controller {
  name = "boundary-zero-trust-controller"
  database {
    url = "env://BOUNDARY_PG_URL"
  }
}

listener "tcp" {
  address = "0.0.0.0:9200"
  purpose = "api"
  tls_disable = false
  tls_cert_file = "/etc/boundary/cert.pem"
  tls_key_file = "/etc/boundary/key.pem"
}