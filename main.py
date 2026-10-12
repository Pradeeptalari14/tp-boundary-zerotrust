#!/usr/bin/env python3
"""
HashiCorp Boundary Session Connect & Ephemeral Target Router
"""
import subprocess
import os

def connect_private_target(target_id: str, local_port: int = 5432):
    print(f"🔐 Establishing zero-trust session to target {target_id} on localhost:{local_port}...")
    cmd = [
        "boundary", "connect", "postgres",
        "-target-id", target_id,
        "-listen-port", str(local_port)
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    connect_private_target("ttcp_1234567890")
