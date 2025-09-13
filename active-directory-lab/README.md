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
- **Automation:** PowerShell script to create countless users**  

---

## 🚀 Skills Demonstrated  
✔️ Windows Server installation & configuration  
✔️ Active Directory Domain Services setup  
✔️ User & group management (manual + automated via PowerShell)  
✔️ DHCP scope & DNS configuration  
✔️ Group Policy Objects (GPOs) for access control  
✔️ Virtualization with Oracle VirtualBox  
✔️ Troubleshooting network & domain issues  

## 🖼️ Screenshot Documentation

1. **Network Architecture Diagram**  
![image alt](https://github.com/bilal2997/cybersecuirty-portfolio/blob/main/active-directory-lab/lab%201%20screenshot%201%20.png?raw=true)
**Description:** Shows the complete VMware network design with NIC configurations, IP addressing scheme (`172.16.0.0/24`), and service allocations. Demonstrates understanding of network segmentation with internal and external adapters, DHCP scope planning (`172.16.0.100-200`), and DNS configuration pointing to the domain controller.

2. **Windows Server 2019 Installation**  
![Windows Server Installation](https://github.com/bilal2997/cybersecuirty-portfolio/blob/main/active-directory-lab/%E5%96%87%E5%8F%AD1%20screens%E5%90%8E%E5%8F%B02%20.png?raw=true)  
**Description:** Captures the Windows Server 2019 installation process within Oracle VirtualBox. Shows successful OS deployment that will serve as the foundation for the domain controller and essential network services.

3. **System Configuration**  
![System Configuration](https://github.com/bilal2997/cybersecuirty-portfolio/blob/main/active-directory-lab/lab%201%20screenshot%203.png?raw=true)  
**Description:** Displays the Server 2019 system properties confirming the evaluation version installation, hardware allocation (2GB RAM), and basic system identification. Important for documenting the lab environment specifications.

4. **IPv4 Network Configuration**  
![IPv4 Network Configuration](./screenshots/04-ipv4-configuration.png)  
**Description:** Shows the TCP/IPv4 configuration for the internal network interface. Documents the static IP assignment (`172.16.0.1`), subnet mask (`255.255.255.0`), and DNS settings that establish the domain controller's network identity.

5. **Active Directory Management Console**  
![Active Directory Management](./screenshots/05-ad-management.png)  
**Description:** The Active Directory Users and Computers (ADUC) console showing the domain structure, organizational units, and user accounts. Demonstrates practical AD management including OU design and user object management.

6. **RAS/NAT Configuration**  
![RAS/NAT Configuration](./screenshots/06-ras-nat-configuration.png)  
**Description:** Routing and Remote Access configuration showing NAT setup that enables internet connectivity for the internal network while maintaining security. Critical for enterprise network design understanding.

7. **DHCP Management Console**  
![DHCP Management](./screenshots/07-dhcp-management.png)  
**Description:** DHCP server management showing scope configuration, IP address range (`172.16.0.100-200`), and options including gateway and DNS server settings. Demonstrates dynamic IP allocation setup for client machines.

8. **PowerShell Automation Script**  
![PowerShell Automation](./screenshots/08-powershell-automation.png)  
**Description:** Showcases the custom PowerShell script that automates bulk user creation (1,000+ users) from a text file. Highlights scripting skills and automation capabilities for enterprise user management.

9. **Client Domain Join**  
![Client Domain Join](./screenshots/09-client-domain-join.png)  
**Description:** Windows 10 client successfully joined to the domain, showing computer object in AD and network connectivity. Demonstrates endpoint integration with domain services.

10. **Network Connectivity Testing**  
![Network Connectivity Testing](./screenshots/10-network-testing.png)  
**Description:** Command prompt showing successful ping tests to both external resources (`google.com`) and internal domain resources (`mydomain.com`). Validates DNS resolution, network connectivity, and domain functionality.
