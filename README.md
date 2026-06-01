# ops345-aws-cloud-infrastructure
AWS cloud infrastructure project demonstrating Linux administration, networking, storage management, web services, and disaster recovery using Amazon Linux and AWS.

# OPS345 AWS Cloud Infrastructure Project

## Overview

This project documents the design, deployment, security, storage management, and application hosting of a multi-tier cloud environment built in Amazon Web Services (AWS) as part of the OPS345 course.

The environment includes:

* Custom AWS VPC and subnet architecture
* Internet Gateway and Route Tables
* EC2 Linux servers
* Security Groups and network isolation
* Persistent storage using EBS volumes
* Cloud application deployment using Apache, PHP, MariaDB, Amazon RDS, and Nextcloud
* Backup and disaster recovery concepts

## Architecture

The infrastructure consists of:

* Router Instance (10.3.45.10)
* Web Server Instance (10.3.45.11)
* Database Services
* Internet Gateway
* Route Tables
* Security Groups
* Persistent Storage Volumes

## Labs Completed

### Lab 1 – AWS Foundation

* Created AWS infrastructure
* Launched EC2 instances
* Configured hostnames and SSH access
* Verified Linux server deployment

### Lab 2 – Network Infrastructure

* Created custom VPC (10.3.45.0/24)
* Created subnet (10.3.45.0/25)
* Configured Internet Gateway
* Configured Route Tables
* Implemented NAT and port forwarding
* Verified secure access to private instances

### Lab 3 – Persistent Storage and Recovery

* Created and attached EBS volumes
* Configured LVM
* Created Logical Volumes
* Mounted persistent storage
* Verified filesystem recovery and persistence

### Lab 4 – Cloud Application Deployment

* Configured Amazon RDS (MariaDB)
* Connected EC2 web server to RDS
* Installed Apache, PHP, and MariaDB client tools
* Deployed Nextcloud
* Configured database users and permissions
* Verified successful web application deployment

## Repository Structure

```text
Lab1-AWS-Foundation/
Lab2-Network-Infrastructure/
Lab3-Persistent-Storage-Recovery/
Lab4-Cloud-Application-Deployment/
diagrams/
```

## Skills Demonstrated

* Linux Administration
* AWS Cloud Infrastructure
* VPC Networking
* Routing and NAT
* Security Groups
* Storage Management (EBS/LVM)
* Database Administration
* Web Application Deployment
* Apache Web Server
* MariaDB / Amazon RDS
* Nextcloud Administration
* Troubleshooting and Recovery
