#!/usr/bin/env bash
# Using puppet to connect without password

file { '/etc/ssh/ssh_config':
    ensure  => present,
    content => "# SSH client configuration
                Host *
                IdentityFile ~/.ssh/school
                PasswordAuthentication no",
}
