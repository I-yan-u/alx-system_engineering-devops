# Updates the number of the Hard and Soft file allowed for User Holberton.

exec { 'Upgrade Holberto"s Hardfile limit':
  command => 'sed -i "s/nofile 5/nofile 10000/" /etc/security/limits.conf',
  path    => 'bin'
}

exec {'Upgrade Holberton"s Soft file limit':
  command => 'sed -i "s/nofile 4/ nofile 10000/" /etc/security/limits.conf',
  path    => 'bin'
}
