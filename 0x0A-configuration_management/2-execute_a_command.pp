# manifest create a manifest that kills a process named killmenow

exec {'killme_process':
    command => '/usr/bin/pkill killmenow'
}