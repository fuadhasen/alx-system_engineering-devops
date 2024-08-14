# puppet manifest that fix apache2 error

exec {'edit_file_extension':
command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
path    => '/usr/local/bin/:/bin/'
}
