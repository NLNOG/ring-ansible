#!/bin/sh
# from https://blog.erincall.com/p/using-pgp-to-encrypt-the-ansible-vault
# NB 20260730 above url is dead, see https://web.archive.org/web/20180222214835///blog.erincall.com/p/using-pgp-to-encrypt-the-ansible-vault for an archived version
gpg --batch --use-agent --decrypt vault_passphrase.gpg
