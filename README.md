# Ansible Practical Examples

Welcome to the **Ansible Practical Examples** repository! This collection is designed to provide a range of Ansible playbooks and tasks, from basic to advanced, to help you learn and effectively use Ansible for configuration management and automation.

## Table of Contents

- [Ansible Practical Examples](#ansible-practical-examples)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Examples](#examples)
    - [Basic Examples](#basic-examples)
    - [Day-to-Day Work Examples](#day-to-day-work-examples)


## Introduction

This repository contains a variety of Ansible playbooks demonstrating different tasks and configurations. Whether you're new to Ansible or looking to expand your knowledge with practical, everyday examples, you'll find valuable resources here.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Ansible (version 2.15 or later)
- Python (version 3.9 or later)
- SSH access to your target hosts
- [Basic concepts](https://paulomenon.github.io/) 

### Installation

To install Ansible, follow these steps:

1. **Using pip**:
    ```sh
    pip install ansible
    ```

2. **Using package manager (Ubuntu example)**:
    ```sh
    sudo apt update
    sudo apt install ansible
    ```
3. **Using package manager (Fedora example)**:
    ```sh
    sudo dnf install ansible
    ```
4. **Using package manager (Mac example)**:
    ```sh
    sudo brew install ansible
    ```


For detailed installation instructions, refer to the [official Ansible installation guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

## Examples

### Basic Examples

These examples cover the fundamental concepts of Ansible, including:

- Setting up your first playbook
- Use Variables and Passing extra vars via command line
- Managing users and groups
- Installing Apps/Softwares
- Copying files
- Basic Jinga2 Templates


### Day-to-Day Work Examples

These examples demonstrate practical Ansible tasks you might encounter in daily operations:

- Configuring web servers
- Setting up databases
- Automating deployments
- Deploy your application on Cloud
- Automating Cloud set up
- Decrypt base64 content
- Practical Jinga2 Templates
- Security updates and patches
- LDAP
- CyberArk
- Network
- Zos IBM Mainframe

Explore the [examples directory](./examples) for simple examples and the [day-to-day-work-examples](./day-to-day-work-examples) for detailed playbooks and documentation.

