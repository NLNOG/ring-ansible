#!/bin/bash
# Run ring-ansible from a local checkout (for development)

export ANSIBLE_FORCE_COLOR=1

/usr/bin/ansible-pull --full -d $(pwd) \
    -U https://github.com/NLNOG/ring-ansible.git \
    --vault-password-file=/root/.vaultpw \
    -i nodes \
    -l $(hostname) \
    -c local \
    -f $@ playbook.yml
