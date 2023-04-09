# Load balancer
![Web infrastructure](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png?raw=true "Web Infrastructure")

### Concepts
- [Load balancer](https://intranet.alxswe.com/concepts/46)
- [Web Stack debuhhing](https://intranet.alxswe.com/concepts/68)
### Resources
- [Introduction to load-balancing and HAproxy](https://intranet.alxswe.com/rltoken/B7f3oz8i3Xvvom_YQZzLnQ)
- [HTTP header](https://intranet.alxswe.com/rltoken/sZ9v3Vq2tgLwN_PWVQketw)
- [Debian/Ubuntu HAProxy packages](https://intranet.alxswe.com/rltoken/2VRAgtKKR9g6Xfb0xzGiSg)

You have been given 2 additional servers:

- gc-[STUDENT_ID]-web-02-XXXXXXXXXX
- gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
Let’s improve our web stack so that there is redundancy for our web servers.
This will allow us to be able to accept more traffic by doubling the number of
web servers, and to make our infrastructure more reliable. If one web server fails,
we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work.
All scripts must be designed to configure a brand new Ubuntu server to match
the task requirements.
