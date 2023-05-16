#DEPLOY AND CONFIG

# Fix amount of recievable requests
exec { 'fix no of possible request':
  command => "sed -i 's/15/5000/' /etc/default/nginx",
  path    => '/bin'
} ->

# Restart nginx
exec { 'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d'
}

