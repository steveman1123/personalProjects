#block ips by attempted ftp login
#invalid users that I've noticed:
# administrator, Admin, anonymous, ftp, user, www-data, ftp1, www, admin, db, wwwroot, data, web, user123, test, guest, anyone, system, server

#https://linux-audit.com/blocking-ip-addresses-in-linux-with-iptables/

# use
# journalctl | grep ' - USER '
# to get the lines with the ip's, then check that the listed user is present (if so, block)
# also ensure that ip is not in local block
