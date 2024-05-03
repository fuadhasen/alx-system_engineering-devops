# Install flask using puppet

exec { 'flask_install':
  command   => '/usr/bin/pip3 install flask==2.1.0'
}
