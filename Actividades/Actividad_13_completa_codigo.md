# Códigos de la Activdad 13 todos los problemas

## Problema 1

### Código para el servidor SMTP
```
import smtplib
from email.mime.text import MIMEText

def setup_smtp_server():
    server = smtplib.SMTP_SSL('smtp.example.com', 465)
    server.login('user@example.com', 'password')
    return server

def send_email(server):
    msg = MIMEText('This is a test email.')
    msg['Subject'] = 'SMTP SSL Test'
    msg['From'] = 'user@example.com'
    msg['To'] = 'recipient@example.com'
    server.send_message(msg)
    server.quit()

smtp_server = setup_smtp_server()
send_email(smtp_server)
```
# Código para el servidor IMAP
```

import imaplib

def setup_imap_server():
    mail = imaplib.IMAP4_SSL('imap.example.com')
    mail.login('user@example.com', 'password')
    return mail

def fetch_emails(mail):
    mail.select('inbox')
    result, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    latest_email_id = id_list[-1]
    result, data = mail.fetch(latest_email_id, '(RFC822)')
    raw_email = data[0][1]
    print(raw_email.decode('utf-8'))
    mail.logout()

imap_server = setup_imap_server()
fetch_emails(imap_server)
```

## Problema 2

### Código Python para simulación del protocolo de red personalizado sobre TCP
```
import socket
import struct

def send_message(sock, msg_type, seq_num, data):
    header = struct.pack('!I I', msg_type, seq_num)
    message = header + data.encode()
    sock.sendall(message)

def receive_message(sock):
    header = sock.recv(8)
    msg_type, seq_num = struct.unpack('!I I', header)
    data = sock.recv(1024)  # ajustar según el tamaño esperado del mensaje
    return msg_type, seq_num, data.decode()

def main():
    host = 'localhost'
    port = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print("Server listening on port", port)
    client_sock, addr = server.accept()
    print("Connected by", addr)
```
 
### Simulación de recepción de un mensaje
```

    msg_type, seq_num, data = receive_message(client_sock)
    print("Received:", msg_type, seq_num, data)
```

### Envío de una respuesta
```
    send_message(client_sock, 1, seq_num + 1, "Ack")
    client_sock.close()
    server.close()

if __name__ == '__main__':
    main()
```

## Problema 3

```
import paramiko
from OpenSSL import crypto

def create_ssh_tunnel(user, password, host, remote_host, local_port, remote_port):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password)
    tunnel = client.get_transport().open_channel('direct-tcpip', (remote_host, remote_port),
                                                  ('localhost', local_port))
    return client, tunnel

def main():
    ssh_user = 'admin'
    ssh_password = 'securepassword'
    ssh_host = 'example.com'
    ldap_host = 'ldap.example.com'
    local_ldap_port = 389
    remote_ldap_port = 389
    client, tunnel = create_ssh_tunnel(ssh_user, ssh_password, ssh_host, ldap_host,
                                       local_ldap_port, remote_ldap_port)
    print(f"SSH tunnel established for LDAP on port {local_ldap_port}")
    tunnel.close()
    client.close()

if __name__ == '__main__':
    main()

def create_self_signed_cert(cert_file, key_file):
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 2048)
    cert = crypto.X509()
    cert.get_subject().C = "US"
    cert.get_subject().ST = "California"
    cert.get_subject().L = "San Francisco"
    cert.get_subject().O = "My Company"
    cert.get_subject().OU = "My Organizational Unit"
    cert.get_subject().CN = "mydomain.com"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha256')
    open(cert_file, "wt").write(crypto.dump_certificate(crypto.FILETYPE_PEM,
                                                        cert).decode('utf-8'))
    open(key_file, "wt").write(crypto.dump_privatekey(crypto.FILETYPE_PEM,
                                                      k).decode('utf-8'))

create_self_signed_cert('ldap_cert.pem', 'ldap_key.pem')

```

## Problema 4 
```
from scapy.all import *

def simulate_ip():
    packet = IP(dst="192.168.1.1") / ICMP() / "Hello, this is an IP packet"
    send(packet)

def simulate_icmp():
    icmp_echo = IP(dst="192.168.1.1") / ICMP(type=8, code=0) / "Ping"
    send(icmp_echo)

def simulate_igmp():
    igmp_packet = IP(dst="224.0.0.1") / IGMP(type=0x16, gaddr="224.0.0.1")
    send(igmp_packet)

def simulate_arp():
    arp_request = ARP(pdst='192.168.1.2')
    send(arp_request)

simulate_ip()
simulate_icmp()
simulate_igmp()
simulate_arp()

```
