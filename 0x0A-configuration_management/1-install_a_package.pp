# Using Puppet, install flask from pip3

# Ensure a specific version of Python 3 is installed
package { 'python3':
  ensure   => '3.8.10',
  provider => 'pip3'
}

# Ensure a specific version of Werkzeug is installed
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

# Ensure that required development packages are installed
package { ['libffi-dev', 'libssl-dev', 'python3-dev']:
  ensure => installed,
}

# Execute a command to install Flask using pip3, version 2.1.0
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}
