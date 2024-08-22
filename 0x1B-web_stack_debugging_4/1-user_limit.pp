# soft and hard limit

exec { 'increase_hard_limits':
  command => "/usr/bin/env sed -i 's/holberton hard nofile [0-9]*/holberton hard nofile 65535/' /etc/security/limits.conf",
  path    => ['/usr/bin', '/bin'],
}

exec { 'increase_soft_limits':
  command => "/usr/bin/env sed -i 's/holberton soft nofile [0-9]*/holberton soft nofile 65535/' /etc/security/limits.conf",
  path    => ['/usr/bin', '/bin'],
}
