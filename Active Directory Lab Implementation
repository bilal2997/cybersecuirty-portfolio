# 🖥️ Active Directory Home Lab  

![Active Directory](https://img.shields.io/badge/Active%20Directory-Enterprise-blue)  
![Windows Server](https://img.shields.io/badge/Windows-Server%202019-red)  
![PowerShell](https://img.shields.io/badge/PowerShell-Automation-blueviolet)  

A hands-on **Active Directory lab environment** built in VirtualBox, showcasing enterprise-level IT skills including **domain services, DNS/DHCP, Group Policies, and PowerShell automation**.  

This project demonstrates my ability to **deploy, configure, and manage** a Windows Server environment, simulating a real-world IT infrastructure.  

---

## 📋 Lab Overview  
- **Domain Controller:** Windows Server 2019 (Server19-DC)  
- **Domain:** `mydomain.com`  
- **Client:** Windows 10 Enterprise VM  
- **Services:** AD DS, DNS, DHCP, NAT/RAS  
- **Automation:** PowerShell script to create **1,000+ users**  

---

## 🚀 Skills Demonstrated  
✔️ Windows Server installation & configuration  
✔️ Active Directory Domain Services setup  
✔️ User & group management (manual + automated via PowerShell)  
✔️ DHCP scope & DNS configuration  
✔️ Group Policy Objects (GPOs) for access control  
✔️ Virtualization with Oracle VirtualBox  
✔️ Troubleshooting network & domain issues  

---

## 🖼️ Screenshots  

### 1️⃣ Network Architecture  
![Network Diagram](screenshots/lab-diagram.png)  

### 2️⃣ Windows Server Installation  
![Server Install](screenshots/windows-server-install.png)  

### 3️⃣ System Configuration & Renaming to DC  
![Rename DC](screenshots/rename-dc.png)  

*(more screenshots will be added as I complete the lab documentation)*  

---

## 💻 PowerShell Automation  

I automated bulk user creation in Active Directory with **PowerShell**:  

```powershell
# Bulk user creation script
Import-Csv .\users.csv | ForEach-Object {
    New-ADUser -Name $_.Name `
               -SamAccountName $_.Sam `
               -UserPrincipalName $_.UPN `
               -AccountPassword (ConvertTo-SecureString "Password123!" -AsPlainText -Force) `
               -Enabled $true
}
