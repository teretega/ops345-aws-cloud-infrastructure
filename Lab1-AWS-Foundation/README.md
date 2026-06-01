# Lab 1 – AWS Foundation

## Objective

The goal of Lab 1 was to become familiar with the AWS environment and deploy the first Amazon EC2 instance that would later become part of the OPS345 cloud infrastructure.

## Technologies Used

- Amazon Web Services (AWS)
- Amazon EC2
- Amazon Linux 2023
- SSH
- Linux Administration

## Tasks Completed

### 1. Launch EC2 Instance

Created an Amazon EC2 instance running Amazon Linux 2023.

### 2. Configure SSH Access

Connected securely to the instance using SSH and a private key.

Example:

```bash
ssh -i ops345-first-key.pem otere@<public-ip>
```

### 3. Configure Hostname

Changed the hostname to:

```text
first.otere.ops345.ca
```

Verification:

```bash
hostnamectl
```

### 4. Verify Operating System

Verified:

- Amazon Linux 2023
- Kernel Version
- Architecture
- Virtualization Platform

## Skills Learned

- AWS EC2 Deployment
- Linux Server Administration
- SSH Connectivity
- Hostname Configuration
- Basic Cloud Infrastructure Management

## Verification Screenshots

### Hostname Configuration

![Lab1 Screenshot 1](Screenshot 2024-01-22 182104.png)

## Outcome

Successfully deployed and configured the first AWS EC2 instance that serves as the foundation for subsequent OPS345 cloud infrastructure labs.