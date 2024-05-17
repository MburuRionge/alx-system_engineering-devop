# enables the user holberton to login and open files without error

# increases hard file limit for Holberton user
exec { 'increases-hard-file-limit-for-holberton-user':
	command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
	path => '/usr/local/bin/:/bin/'
}

# Increases soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
	command => 'sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf',
	path => '/usr/local/bin/:/bin/'
}
