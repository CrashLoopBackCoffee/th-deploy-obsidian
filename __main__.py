"""A Python Pulumi program"""

import pulumi
import pulumi_docker

config = pulumi.config.Config()

target_host = config.get("target-host")

provider = pulumi_docker.Provider("synology", host=f"ssh://{target_host}")

opts = pulumi.ResourceOptions(provider=provider)

# Create networks so we don't have to expose all ports on the host
network = pulumi_docker.Network("obsidian", opts=opts)
