# Incident Response Playbook: Ransomware and Phishing Simulation

## Ransomware Simulation
1. **Preparation**: Ensure VM snapshots, auditd active (`sudo systemctl status auditd`).
2. **Identification**: Check logs: `sudo ausearch -k file_changes`.
3. **Containment**: Isolate network: `sudo ip link set enp0s3 down`.
4. **Eradication**: Remove malicious files: `rm /home/vboxuser/TestFiles/*.encrypted && rm /home/vboxuser/ransom_sim.py`.
5. **Recovery**: Revert snapshot or recreate files; re-enable network: `sudo ip link set enp0s3 up`.
6. **Lessons**: Log in `incident_log.txt`, analyze gaps.

## Phishing Simulation
1. **Identification**: Monitor with Wireshark on Kali (`sudo wireshark`, filter `http.request.method == POST`) or Wazuh alerts.
2. **Containment**: Block attacker: `sudo iptables -A INPUT -s 192.168.100.10 -j DROP`.
3. **Eradication**: Stop SET on Kali (Ctrl+C).
4. **Recovery**: Reset credentials, educate user.