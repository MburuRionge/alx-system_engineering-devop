#!/usr/bin/env bash
# Using puppet to connect without password

file { '/etc/ssh/ssh_config':
	ensure => present,
}
file_line { 'Turn off password authenticator':
	path => '/etc/ssh/ssh_config',
	line => 'Passwwordauthentication no',
	match => '^#PasswordAuthentication',
}
file_line { 'Declare identity file':
	path => '/etc/ssh/ssh_config',
	line => 'IdentityFile ~/.ssh/school',
	match => '^#IdentityFile',
}
