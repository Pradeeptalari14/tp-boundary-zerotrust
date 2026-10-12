# HashiCorp Boundary Zero-Trust Access Studio

> **Production Repository:** `Pradeeptalari14/tp-boundary-zerotrust`  
> **Interactive Studio Workspace:** [https://talaripradeep.info/tools/hashicorp-boundary-zerotrust/](https://talaripradeep.info/tools/hashicorp-boundary-zerotrust/)  
> **Visual Flow Canvas:** [https://talaripradeep.info/studios/flow/?studio=hashicorp-boundary-zerotrust](https://talaripradeep.info/studios/flow/?studio=hashicorp-boundary-zerotrust)

## Overview
Deploy identity-based zero-trust remote access for EKS clusters and Aurora databases without SSH keys, open bastion ports, or legacy static VPN credentials.

## Primary Specification Manifest: `boundary-controller.hcl`
```yaml
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
```

## Verification & Execution
```bash
# Run local verification
git verify-commit HEAD
```

## License
MIT License. Copyright (c) 2026 Talari Pradeep.
