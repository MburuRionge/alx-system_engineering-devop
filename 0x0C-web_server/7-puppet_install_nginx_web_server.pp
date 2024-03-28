# Setup New Ubuntu server with nginx

exec { 'update system':
    command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure  => 'installed',
    require => Exec['update system'],
}

file { '/var/www/html/index.html':
    content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => template('module_name/default_config.erb'),
    notify  => Service['nginx'],
}

service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
}
File['/etc/nginx/sites-available/default'] ~> Service['nginx']
