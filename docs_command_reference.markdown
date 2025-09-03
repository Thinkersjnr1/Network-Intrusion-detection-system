# Command Reference: Incident Response Simulation Tool

This file lists all commands used in the Incident Response Simulation Tool project, organized by phase and platform (Kali Linux: attacker at `192.168.100.10`; Ubuntu: victim at `192.168.100.20`, username `vboxuser`). Use this as a quick reference to execute the project steps.

## Phase 1: Preparation and Verification (30-45 mins)

### Kali Linux
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install tools
sudo apt install metasploit-framework wireshark set -y

# Install Python packages
pip3 install cryptography
```

### Ubuntu
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install tools
sudo apt install auditd sysstat -y

# Install Python packages
pip3 install --user cryptography schedule pandas scikit-learn numpy

# Verify hardware
free -h
df -h
lscpu | grep Virtualization

# Verify auditd
systemctl status auditd

# Verify Python packages
pip3 show cryptography
```

## Phase 2: Set Up Virtual Lab Environment (1-1.5 hours)

### Kali Linux
```bash
# Configure static IP
sudo nano /etc/netplan/01-netcfg.yaml
# Add:
# network:
#   version: 2
#   ethernets:
#     enp0s3:
#       dhcp4: no
#       addresses: [192.168.100.10/24]
sudo netplan try
sudo netplan apply

# Verify IP
ip a

# Test connectivity
ping 192.168.100.20
```

### Ubuntu
```bash
# Configure static IP
sudo nano /etc/netplan/01-netcfg.yaml
# Add:
# network:
#   version: 2
#   ethernets:
#     enp0s3:
#       dhcp4: no
#       addresses: [192.168.100.20/24]
sudo netplan try
sudo netplan apply

# Verify IP
ip a

# Test connectivity
ping 192.168.100.10

# Configure auditd rule
sudo nano /etc/audit/rules.d/audit.rules
# Add:
# -w /home/vboxuser/TestFiles -p wa -k file_changes
sudo systemctl restart auditd

# Verify rule
sudo auditctl -l

# Create test directory and files
mkdir -p /home/vboxuser/TestFiles
echo "Data 1" > /home/vboxuser/TestFiles/secret1.txt
echo "Data 2" > /home/vboxuser/TestFiles/secret2.txt
echo "Data 3" > /home/vboxuser/TestFiles/secret3.txt

# Verify files
ls -l /home/vboxuser/TestFiles
```

## Phase 3: Design Scenario and Playbook (45-60 mins)

### Kali Linux
```bash
# Create and edit ransom_sim.py
nano /home/kali/ransom_sim.py
# Add content from scripts/ransom_sim.py (see repo)

# Transfer to Ubuntu
scp /home/kali/ransom_sim.py vboxuser@192.168.100.20:/home/vboxuser/

# Create playbook
nano IR_Playbook.md
# Add content from docs/IR_Playbook.md (see repo)
```

### Ubuntu
```bash
# Make script executable
chmod +x /home/vboxuser/ransom_sim.py

# Verify script
cat /home/vboxuser/ransom_sim.py

# Verify test files
ls /home/vboxuser/TestFiles
```

## Phase 4: Execute the Simulation (30-45 mins)

### Kali Linux
```bash
# Monitor network (optional)
sudo wireshark &
```

### Ubuntu
```bash
# Start monitoring logs
sudo tail -f /var/log/audit/audit.log

# Run ransomware simulation
python3 /home/vboxuser/ransom_sim.py

# Detect
sudo ausearch -k file_changes

# Contain
sudo ip link set enp0s3 down

# Eradicate
rm /home/vboxuser/TestFiles/*.encrypted
rm /home/vboxuser/ransom_sim.py

# Recover
# Option 1: Recreate files
echo "Data 1" > /home/vboxuser/TestFiles/secret1.txt
echo "Data 2" > /home/vboxuser/TestFiles/secret2.txt
echo "Data 3" > /home/vboxuser/TestFiles/secret3.txt
# Option 2: Revert VirtualBox snapshot

# Re-enable network
sudo ip link set enp0s3 up

# Verify files
ls /home/vboxuser/TestFiles

# Log times
nano /home/vboxuser/incident_log.txt
# Add:
# Attack Start: 22:00
# Detected: 22:02
# Contained: 22:03
# Eradicated: 22:04
# Recovered: 22:05
```

## Phase 5: Evaluate and Iterate (30 mins)

### Kali Linux
```bash
# Phishing simulation
sudo setoolkit
# Select: 1) Social-Engineering Attacks > 2) Website Attack Vectors > 3) Credential Harvester Attack > 2) Site Cloner
# IP: 192.168.100.10, Port: 80, URL: https://accounts.google.com

# Allow port
sudo ufw allow 80

# Verify server
curl http://192.168.100.10
sudo netstat -tuln | grep 80

# Create phishing email template
nano phishing_email.txt
# Add:
# Subject: Urgent: Verify Your Google Account
# Please login to verify your account: http://192.168.100.10
```

### Ubuntu
```bash
# Install dependencies for metrics and AI
pip3 install --user pandas scikit-learn numpy schedule

# Create and run metrics script
nano metrics.py
# Add content from scripts/metrics.py (see repo)
python3 metrics.py

# Create and test anomaly detection (future)
nano anomaly_detection.py
# Add content from scripts/anomaly_detection.py (see repo)
# Create sample CSV
nano audit_log.csv
# Add:
# timestamp,event_type
# 2025-09-03 22:01:00,unlink
# 2025-09-03 22:01:01,openat
# 2025-09-03 22:01:02,unlink
python3 anomaly_detection.py

# Create and run automation script
nano auto_sim.py
# Add content from scripts/auto_sim.py (see repo)
python3 auto_sim.py

# Update incident log
nano incident_log.txt
# Add:
# Gaps: Slow detection (2 mins)—consider Wazuh email alerts.
# Improvements: Integrate phishing, automate runs.

# Test phishing page
curl http://192.168.100.10
firefox http://192.168.100.10

# Verify logs
sudo ausearch -k file_changes
sudo less /var/log/audit/audit.log | grep file_changes
```

## Troubleshooting Commands

### Kali Linux
```bash
# Check network
ip a
ping 192.168.100.20
sudo ufw status
sudo ufw allow 80

# Reinstall SET
sudo apt install set -y

# Check Apache
sudo systemctl status apache2
sudo systemctl restart apache2
```

### Ubuntu
```bash
# Check network
ip a
ping 192.168.100.10
sudo ufw status
sudo ufw allow from 192.168.100.10

# Fix auditd
sudo auditctl -w /home/vboxuser/TestFiles -p wa -k file_changes
sudo systemctl restart auditd
sudo auditctl -l

# Reinstall Python packages
pip3 install --user --upgrade pip
pip3 install --user cryptography schedule pandas scikit-learn numpy
```