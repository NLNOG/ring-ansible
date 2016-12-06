#!/bin/sh
# from https://blog.erincall.com/p/using-pgp-to-encrypt-the-ansible-vault
gpg --batch --use-agent --decrypt vault_passphrase.gpg
