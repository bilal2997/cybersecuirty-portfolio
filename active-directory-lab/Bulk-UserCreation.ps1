<#
.SYNOPSIS
Active Directory Bulk User Creation Script

.DESCRIPTION
This PowerShell script automates the creation of multiple user accounts in Active Directory
from a text file containing first and last names. It creates standardized usernames and
places all users in a dedicated Organizational Unit.


.REQUIREMENTS
- Active Directory PowerShell Module
- Appropriate permissions to create users and OUs
#>

# ---------- #
$PASSWORD_FOR_USERS   = "Password1"    # Default password for all new users
$USER_FIRST_LAST_LIST = Get-Content .\names.txt  # Text file with "First Last" names
# ------------------------------------------------------ #

# Convert plain text password to secure string for security
$password = ConvertTo-SecureString $PASSWORD_FOR_USERS -AsPlainText -Force

# Create a new Organizational Unit to store all the users
# ProtectedFromAccidentalDeletion $false allows the OU to be deleted if needed
New-ADOrganizationalUnit -Name _USERS -ProtectedFromAccidentalDeletion $false

# Loop through each name in the text file
foreach ($n in $USER_FIRST_LAST_LIST) {
    # Split the full name into first and last components
    $first = $n.Split(" ")[0].ToLower()  # Convert to lowercase for consistency
    $last = $n.Split(" ")[1].ToLower()   # Convert to lowercase for consistency
    
    # Generate username using first initial + last name (e.g., jsmith)
    $username = "$($first.Substring(0,1))$($last)".ToLower()
    
    # Display progress in the console
    Write-Host "Creating user: $($username)" -BackgroundColor Black -ForegroundColor Cyan
    
    # Create the new Active Directory user with all properties
    New-AdUser -AccountPassword $password `              # Set the password
               -GivenName $first `                       # First name
               -Surname $last `                          # Last name
               -DisplayName $username `                  # Display name
               -Name $username `                         # Full name
               -EmployeeID $username `                   # Employee ID (using username)
               -PasswordNeverExpires $true `             # Password doesn't expire
               -Path "ou=_USERS,$(([ADSI]`"").distinguishedName)" `  # Place in _USERS OU
               -Enabled $true                            # Enable the account immediately
}

# Script completion
Write-Host "User creation process completed!" -ForegroundColor Green
Write-Host "All users have been created in the _USERS Organizational Unit" -ForegroundColor Yellow
