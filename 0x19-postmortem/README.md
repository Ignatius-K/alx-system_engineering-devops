# 19-August-2024: Company Website Failure Review

## Summary about the incident
The company website failed from **19-08-2024 00:10 EAT** to **19-08-2024 01:40 EAT**.\
The website was not accessible, all users who tried to access the site encountered 
a **500 Internal Server Error page**.\
This was due to a file not being pushed in the new website version.

## Timeline of the incident
**00:10 EAT** - Customer reaches out via company email expressing how they can't
                access the site\
**00:11 EAT** - We, the Technical team are notified about the issue.\
**00:15 EAT** - Assumptions are made on the root cause of the issue, checks are made
                on the server and system.\
                The web service was checked, to ensure its running
                The service's status was checked, but it was running and ok
                The service was restarted, to check if the issue is consistent and the
                issue persisted\
**01:36 EAT** - Using **strace**, the service process was monitored, and cause of issue was
                attained and resolved\
**01:38 EAT** - Puppet mainfest file containing the fix was deployed on master server and
                applied across all servers.

## Root cause of the incident
During development, a file with an extension of ".phpp" was being used and was being
imported and depended on by other resources. \
On pushing the code, our company tool "the file validator" changed the file to its expected
file type that is ".php".\
Hence, when deployed the file with ".phpp" was not accessible to the web server causing a
500 Internal server Error.

## Resolution
A puppet manifest file was written with fix and pushed to the master server.\
Then, by puppet's power the fix was applied to all other servers.\
The fix involved moving the file with ".php" extension to the required one ".phpp"

## Preventative measures recommended
- The "file validator" should be redesigned to be interactive
- A staging server should be put in place for testing, before code is pushed to production
