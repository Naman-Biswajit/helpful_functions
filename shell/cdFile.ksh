#!/usr/bin/env ksh
#
# change directory to that of the specified file
#
# add the following alias in `/etc/profile` to get a nicer alias
# alias cdf='. cdFile.ksh '
# 
# 
# Usage:
# ~> cdf /usr/share/tomcat/logs/catalina.out
# goes to:
# /user/share/tomcat/logs> 


cd $(dirname $1)
