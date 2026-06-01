# Lab 4 – Cloud Application Deployment (Nextcloud)

## Objective

The goal of Lab 4 was to deploy a production-style cloud application using a multi-tier architecture consisting of:

- Web Server Layer
- Database Layer
- Cloud Storage Application

The application deployed was Nextcloud, an open-source file sharing and collaboration platform.

---

## Technologies Used

- Amazon Web Services (AWS)
- Amazon EC2
- Amazon RDS
- MariaDB
- Apache HTTP Server
- PHP
- Nextcloud
- Linux Administration

---

## Architecture

### Application Tier

Web Server:

```text
www
10.3.45.11
```

### Database Tier

Amazon RDS MariaDB

```text
ops345db
```

### Application

```text
Nextcloud
```

Users access Nextcloud through the web server while application data is stored in Amazon RDS.

---

## Tasks Completed

### 1. Create Amazon RDS Database

Created an Amazon RDS MariaDB instance:

```text
ops345db
```

Configuration:

- MariaDB Engine
- db.t3.micro
- Port 3306

Purpose:

Provide a managed database service for Nextcloud.

---

### 2. Configure Database Users

Created database users for application access.

Verified user accounts:

```sql
SELECT user FROM user;
```

---

### 3. Create Application Database

Created databases for application storage.

Verified databases:

```sql
SHOW DATABASES;
```

---

### 4. Install Apache and PHP

Installed:

```bash
httpd
php
php-mysqlnd
```

Configured Apache to host Nextcloud.

---

### 5. Install Nextcloud

Downloaded and deployed Nextcloud.

Configured:

- Database connection
- Storage location
- Administrative account

---

### 6. Configure RDS Connectivity

Connected the web server to Amazon RDS.

Verified:

- Database connectivity
- User authentication
- Application database access

---

### 7. Verify Application Deployment

Successfully accessed:

```text
http://<server-ip>/nextcloud
```

Verified:

- Dashboard access
- User login
- File storage functionality

---

## Skills Learned

- AWS RDS Administration
- MariaDB Management
- Web Application Deployment
- Apache Administration
- PHP Configuration
- Nextcloud Administration
- Cloud Storage Platforms
- Multi-Tier Architecture
- Database Connectivity
- Application Troubleshooting

---

## Verification Screenshots

### Amazon RDS Database

![RDS Database](screenshots/S1.png)

### Database User Verification

![Database Users](screenshots/S2.png)

### Database Verification

![Database Verification](screenshots/S3.png)

### Nextcloud Dashboard

![Nextcloud Dashboard](screenshots/S4.png)

---

## Outcome

Successfully deployed a cloud-based file sharing platform using Nextcloud, integrated with Amazon RDS MariaDB, demonstrating the deployment and management of a multi-tier cloud application architecture.