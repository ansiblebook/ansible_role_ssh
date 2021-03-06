# ansible_role_ssh
Improve the security settings of the [OpenSSH](https://www.openssh.com/) SSH server.

## Legal

The countries in which your servers currently reside may have restrictions on the import, possession, use, and/or re-export to another country, of encryption software. BEFORE using any encryption software, please check your country's laws, regulations and policies concerning the import, possession, or use, and re-export of encryption software, to see if this is permitted. See http://www.wassenaar.org/ for more information.

# What does this role change?

This role is based on audit findings using [ssh-audit](https://github.com/jtesta/ssh-audit). This role will improve the crypto of your ssh server to more secure and faster settings.

- When crypto policies are available the configured policy is set and activated, although a reboot is recommended.
- Crypto is configured in way that ssh-audit passes without warnings.
- The  Diffie Hellmann moduli size for sshd is adjusted to modern standards.
- Host keys are re-configured from RSA to ED25519, this is faster and more secure. An RSA host key is now considered weak [source](https://eprint.iacr.org/2020/014.pdf).
- RSA and ECDSA host keys are disabled in sshd.

## Crypto Policies

Crypto policies were introduced in Fedora 21 and are also used in RHEL8, Centos Stream, Ubuntu 20. The STRICT policy template defines modern crypto for SSH and TLS that is stronger than FIPS:OSPP. The configured crypto policy will be system-wide for all applications. You can configure the policies present on your system too, but this role installs the STRICT crypto policy by default.

### Possible crypto_policy values

`crypto_policy: 'STRICT'` Recommended for high-security systems.

`crypto_policy: 'FUTURE'` Recommended for modern systems.

`crypto_policy: 'FIPS:OSPP'` FIPS with OSPP policy modification (stricter than FIPS).

`crypto_policy: 'FIPS'` Required for (US) Federal Information Processing Standard.

`crypto_policy: 'DEFAULT'` What you get without this role, i.e. "export" quality.

`crypto_policy: 'LEGACY'` Weak, for compatibility with older systems.

## Algorithm recommendations

The recommended crypto is configured in sshd_config when the `STRICT` crypto_policy is selected for a platform without crypto policy support, otherwise the STRICT policy is installed and configured with `update-crypto-policy`.

- `Ciphers: chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr`
- `HostKeyAlgorithms: ssh-ed25519-cert-v01@openssh.com,ssh-ed25519`
- `KexAlgorithms: curve25519-sha256,curve25519-sha256@libssh.org,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256`
- `MACs: hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,umac-128-etm@openssh.com`

## Default Variables

The recommended default is configured in `defaults/main.yml`.
`min_dh_size: '3072'` Minimal Diffie Hellmann moduli size.

# Hardening guides

- https://www.sshaudit.com/hardening_guides.html
- https://infosec.mozilla.org/guidelines/openssh.html
- http://safecurves.cr.yp.to/
- http://static.open-scap.org/


Copyright 2022 Bas Meijer @bbaassssiie
