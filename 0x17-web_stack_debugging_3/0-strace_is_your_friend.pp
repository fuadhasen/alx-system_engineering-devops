# puppet manifest that fix apache2 error

file_line { 'correct file name':
  path  => '/var/www/html/wp-settings.php',
  line  => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
  match => 'require_once\( ABSPATH \. WPINC \. \'/class-wp-locale\.phpp\' \);'
}
