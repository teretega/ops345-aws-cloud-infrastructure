# OPS345 AWS Cloud Infrastructure Project

AWS cloud infrastructure project demonstrating Linux administration, networking, storage management, web services, DNS, HTTPS/TLS, automation, load balancing, and disaster recovery using Amazon Linux and AWS.

## Overview

This repository documents the design, deployment, security, storage management, application hosting, DNS configuration, HTTPS implementation, automation, and load balancing of a multi-server cloud environment built in Amazon Web Services (AWS) as part of the OPS345 course.

The project progresses from foundational AWS infrastructure through networking, persistent storage, application deployment, DNS, HTTPS/TLS security, and multi-server web architecture.

The environment includes:

* Custom AWS VPC and subnet architecture
* Internet Gateway and route tables
* EC2 Linux servers
* Security Groups and network isolation
* Linux router and NAT configuration
* SSH port forwarding
* Persistent storage using Amazon EBS
* Apache and PHP web services
* Amazon RDS / MariaDB
* Nextcloud deployment
* DNS configuration
* AWS Route 53
* DNS A, CNAME, and TXT records
* Let's Encrypt SSL/TLS certificates
* Certbot DNS validation
* Apache HTTPS configuration
* HTTP-to-HTTPS redirection
* HTTPS port forwarding using iptables
* Amazon Machine Images (AMI)
* Multiple synchronized web servers
* SSH key-based server-to-server authentication
* Automated file synchronization using rsync and cron
* iptables-based HTTP load balancing
* Python-based load testing
* Backup and disaster recovery concepts

## Architecture

The environment was progressively expanded throughout the labs and Assignment 1.

The web architecture includes:

```text
                         Internet
                            |
                            v
                  +--------------------+
                  |   Route 53 DNS     |
                  |     otere.org      |
                  +---------+----------+
                            |
                            v
                  +--------------------+
                  |  Router / Load     |
                  |     Balancer       |
                  |    10.3.45.10      |
                  |     iptables       |
                  |   HTTP / HTTPS     |
                  +---------+----------+
                            |
              +-------------+-------------+-------------+
              |             |             |             |
              v             v             v             v
         +---------+   +---------+   +---------+   +---------+
         |   www   |   | slave1  |   | slave2  |   | slave3  |
         | .45.11  |   | .45.21  |   | .45.22  |   | .45.23  |
         +---------+   +---------+   +---------+   +---------+
              \             |             |             /
               \____________|_____________|____________/
                            |
                     Synchronized Web
                         Content
```

### Core Infrastructure

* Router / Load Balancer — `10.3.45.10`
* Main Web Server (`www`) — `10.3.45.11`
* Web Server (`www-slave1`) — `10.3.45.21`
* Web Server (`www-slave2`) — `10.3.45.22`
* Web Server (`www-slave3`) — `10.3.45.23`
* Custom VPC — `10.3.45.0/24`
* Subnet — `10.3.45.0/25`
* Internet Gateway
* Route Tables
* Security Groups
* Amazon EBS persistent storage
* Amazon RDS database services
* Route 53 DNS
* Let's Encrypt TLS certificates

## Labs Completed

### Lab 1 – AWS Foundation

* Created AWS infrastructure
* Launched EC2 instances
* Configured Linux hostnames
* Configured SSH access
* Verified Linux server deployment

### Lab 2 – Network Infrastructure

* Created custom VPC (`10.3.45.0/24`)
* Created subnet (`10.3.45.0/25`)
* Configured Internet Gateway
* Configured Route Tables
* Implemented Linux routing
* Configured NAT and port forwarding
* Verified secure access to private instances

### Lab 3 – Persistent Storage and Recovery

* Created and attached Amazon EBS volumes
* Configured LVM
* Created Logical Volumes
* Created and mounted filesystems
* Configured persistent mounts
* Verified storage persistence
* Practiced filesystem recovery concepts

### Lab 4 – Cloud Application Deployment

* Configured Amazon RDS using MariaDB
* Connected the EC2 web server to RDS
* Installed Apache, PHP, and MariaDB client tools
* Deployed Nextcloud
* Configured database users and permissions
* Configured application storage
* Verified successful web application deployment

### Lab 5 – DNS Configuration

* Configured DNS for the AWS-hosted environment
* Used the `otere.org` domain with AWS Route 53
* Configured DNS A records
* Configured CNAME records
* Verified DNS resolution using `dig`
* Connected the domain name to the existing web infrastructure
* Verified Nextcloud access using the configured domain name

### Lab 6 – HTTPS and SSL/TLS Certificates

* Installed and configured Certbot
* Requested a trusted TLS certificate from Let's Encrypt
* Used DNS TXT validation to prove domain ownership
* Verified the `_acme-challenge` TXT record using `dig`
* Installed Apache `mod_ssl`
* Configured Apache with the Let's Encrypt certificate and private key
* Configured HTTPS on TCP port 443
* Configured iptables DNAT forwarding for HTTPS
* Configured AWS Security Groups for HTTPS traffic
* Verified Apache was listening on TCP 443 using `ss`
* Tested HTTPS connectivity using `curl`
* Troubleshot HTTPS traffic using `tcpdump`
* Identified and corrected a missing router Security Group rule for TCP 443
* Verified secure Nextcloud access over HTTPS
* Configured an HTTP 301 redirect to automatically send HTTP traffic to HTTPS

## Assignments

### Assignment 1 – Web Server Load Balancing

Expanded the AWS environment from a single web server into a four-server web architecture with automated content synchronization and Linux-based load balancing.

Key implementation tasks included:

* Created reusable web-server Amazon Machine Images (AMIs)
* Deployed additional EC2 web servers from AMIs
* Configured EBS storage for web content
* Configured SSH key-based authentication between servers
* Synchronized `/var/www/html` using rsync
* Excluded the Nextcloud directory from synchronization
* Automated synchronization every five minutes using cron
* Configured SSH port forwarding through the router
* Configured iptables DNAT rules for HTTP traffic
* Distributed incoming HTTP traffic across four backend servers
* Used Apache access logs to verify backend requests
* Updated EC2 metadata queries to display each server's private IP
* Created a Python script to automate load testing
* Used curl to generate repeated HTTP requests
* Verified that requests were distributed across all four servers

[View Assignment 1](Assignment1-Web-Server-Load-Balancing/README.md)

## Repository Structure

```text
ops345-aws-cloud-infrastructure/
│
├── Lab1-AWS-Foundation/
│   ├── README.md
│   └── screenshots/
│
├── Lab2-Network-Infrastructure/
│   ├── README.md
│   └── screenshots/
│
├── Lab3-Persistent-Storage-Recovery/
│   ├── README.md
│   └── screenshots/
│
├── Lab4-Cloud-Application-Deployment/
│   ├── README.md
│   └── screenshots/
│
├── Lab5-DNS/
│   ├── README.md
│   └── screenshots/
│
├── Lab6-HTTPS-SSL-Certificates/
│   ├── README.md
│   └── screenshots/
│
├── Assignment1-Web-Server-Load-Balancing/
│   ├── README.md
│   ├── screenshots/
│   └── scripts/
│       └── asg1Test.py
│
├── diagrams/
└── README.md
```

## Skills Demonstrated

### AWS

* Amazon EC2
* Amazon VPC
* Subnets
* Internet Gateways
* Route Tables
* Security Groups
* Amazon EBS
* Amazon Machine Images (AMI)
* Amazon RDS
* Amazon Route 53

### Linux Administration

* Amazon Linux
* Linux networking
* Filesystem administration
* LVM
* SSH
* SSH key-based authentication
* systemd services
* cron / crond
* rsync
* curl
* iptables
* tcpdump
* Apache administration

### Networking

* VPC networking
* CIDR addressing
* Routing
* NAT
* DNAT
* Port forwarding
* Private and public IP addressing
* Security-group configuration
* Multi-server networking
* HTTP traffic distribution
* HTTPS / TCP 443
* DNS resolution

### DNS

* AWS Route 53
* DNS A records
* CNAME records
* TXT records
* DNS ownership validation
* `dig` DNS troubleshooting
* Fully Qualified Domain Names (FQDN)

### Web and Database Services

* Apache HTTP Server
* PHP
* MariaDB
* Amazon RDS
* Nextcloud
* HTTP
* HTTPS

### Security and TLS

* SSL/TLS certificates
* Let's Encrypt
* Certbot
* DNS certificate validation
* Apache `mod_ssl`
* Public/private key concepts
* HTTPS configuration
* HTTP-to-HTTPS redirection
* Security Group configuration
* TLS troubleshooting

### Automation and Testing

* Bash/Linux command-line administration
* Automated file synchronization
* Cron job scheduling
* Python scripting
* HTTP testing with curl
* Load-balancer testing
* Apache access-log analysis

### Troubleshooting

* SSH connectivity
* Security-group rules
* NAT and port-forwarding issues
* Web-server connectivity
* EBS storage
* File permissions
* rsync synchronization
* EC2 Instance Metadata Service (IMDSv2)
* iptables load-balancing rules
* DNS resolution
* Apache SSL configuration
* TCP port troubleshooting
* HTTPS connectivity
* Network packet analysis using `tcpdump`

## Project Outcome

The project evolved from a basic AWS Linux environment into a multi-server cloud architecture with private networking, persistent storage, database services, DNS, secure HTTPS communication, automated content synchronization, and Linux-based load balancing.

DNS was configured to provide domain-based access to the AWS-hosted services. HTTPS was then implemented using a trusted Let's Encrypt TLS certificate, with Apache configured to provide encrypted communication over TCP port 443. HTTP requests are automatically redirected to HTTPS.

The Assignment 1 environment further expanded the architecture by distributing HTTP traffic across four EC2 web servers while rsync and cron maintain consistent web content across the servers. A Python load-testing script was used to validate traffic distribution across the backend servers.

This repository demonstrates hands-on experience with AWS infrastructure, Linux systems administration, networking, DNS, SSL/TLS security, web services, automation, troubleshooting, and scalable cloud architecture.
