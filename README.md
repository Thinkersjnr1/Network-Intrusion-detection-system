# Network-Intrusion-detection-system

Incident Response Simulation Tool

This project simulates a ransomware attack and phishing scenario in a controlled virtual environment to practice incident response (IR) following NIST SP 800-61r2. It uses 

**Kali Linux (attacker)** and **Ubuntu (victim)** with tools like **auditd**, **Social-Engineer Toolkit** (SET), and **Python scripts** for automation and AI detection.

# Overview

Goal: Simulate cyber incidents to test detection, containment, eradication, and recovery.

Environment: VirtualBox VMs (Kali: 192.168.100.10, Ubuntu: 192.168.100.20, username vboxuser).

Tools: Python (cryptography, pandas, scikit-learn, schedule), auditd, Wazuh, SET, Metasploit.

Date: September 3, 2025.

# Prerequisites

Hardware: 16GB RAM, 50GB disk, virtualization enabled (VT-x/AMD-V).

Software:

VirtualBox (download).

Kali Linux ISO (kali.org).

Ubuntu Server ISO (ubuntu.com).

Python 3, pip3 install cryptography schedule pandas scikit-learn numpy.


Network: VMs on Internal Network SimNet, static IPs.

# Setup

**VM Configuration:**
Kali: 4GB RAM, 2 CPUs, 40GB disk.

Ubuntu: Same specs, username vboxuser.

Network: Internal Network SimNet.

IPs: Kali (192.168.100.10), Ubuntu (192.168.100.20).

# Commands:# Kali

sudo nano /etc/netplan/01-netcfg.yaml

# Add:
network:
  
  version: 2
  
   ethernets:
    
    enp0s3:
      
      dhcp4: no
      
      addresses: [192.168.100.10/24]

sudo netplan apply

# Ubuntu (same, but addresses: [192.168.100.20/24])




# Install Tools:

Ubuntu: sudo apt install auditd sysstat -y.

Kali: sudo apt install metasploit-framework wireshark set -y.

Both: pip3 install cryptography schedule pandas scikit-learn numpy.



**Phases**

# Phase 1: Preparation

Verify hardware: free -h, df -h, lscpu | grep Virtualization.

Update: sudo apt update && sudo apt upgrade -y.

# Phase 2: Virtual Lab

Set audit rule on Ubuntu:sudo nano /etc/audit/rules.d/audit.rules

# Add:

-w /home/vboxuser/TestFiles -p wa -k file_changes

sudo systemctl restart auditd

Create test files: mkdir /home/vboxuser/TestFiles; echo "Data" > /home/vboxuser/TestFiles/secret1.txt.

# Phase 3: Scenario and Playbook

Scenario: Ransomware encrypts .txt files in /home/vboxuser/TestFiles.

See docs/IR_Playbook.md and scripts/ransom_sim.py.

# Phase 4: Execute Simulation

Run: python3 /home/vboxuser/ransom_sim.py.

Detect: sudo ausearch -k file_changes.

Respond: Follow playbook.

# Phase 5: Evaluate and Iterate

Metrics: Run scripts/metrics.py.

Lessons: Update docs/incident_log.txt.

Extensions: Phishing (SET), AI detection (scripts/anomaly_detection.py), scheduled runs (scripts/auto_sim.py).

# Repository Structure

scripts/: Python scripts.

docs/: Playbook and logs.

.gitignore: Ignores logs, .pyc files.
