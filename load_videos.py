import paramiko

# SSH connection parameters
hostname = 'gate.bss.phy.cam.ac.uk'
port = 22  # Default port for SSH, adjust if your server uses a different port
username = 'yz655'       # Replace with your username
password = '********'    # Replace with your password

# Connect to the remote server
ssh = paramiko.SSHClient()

# This is used to add the server's host key automatically. s
# In a real-world scenario, you might want to check the host key.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port, username, password)

# Execute a command (for example, list files in a directory)
stdin, stdout, stderr = ssh.exec_command('ls ../../../cicutagroup/crop_data/wheat_videos/drone_videos/drone_videos')
for line in stdout:
    print(line.strip())

# Close the SSH connection
ssh.close()
