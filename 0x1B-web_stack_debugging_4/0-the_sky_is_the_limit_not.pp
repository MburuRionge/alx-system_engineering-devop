# Increases the amount of traffic a Nginx server can serve

exec {'modify max open files limit setting':
	# Modify ULIMIT value
	command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
	path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin/bin:/usr/games:/usr/local/games',
}
