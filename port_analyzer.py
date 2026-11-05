
{
  "msrpc": {
    "severity": "medium",
    "description": "Windows RPC service is exposed.",
    "recommendation": "Restrict RPC access to trusted networks."
  },
  "microsoft-ds": {
    "severity": "high",
    "description": "SMB file sharing is exposed.",
    "recommendation": "Block public SMB access unless required."
  },
  "telnet": {
    "severity": "high",
    "description": "Telnet uses unencrypted communication.",
    "recommendation": "Replace Telnet with SSH."
  },
  "ftp": {
    "severity": "high",
    "description": "FTP may transmit credentials in plaintext.",
    "recommendation": "Use SFTP or FTPS."
  }
}
