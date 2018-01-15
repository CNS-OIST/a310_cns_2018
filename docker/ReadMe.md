# Installing NEURON via docker

1. Install [Docker Community Edition](https://www.docker.com/community-edition).

2. Start Docker.

3. In Windows, also [turn on drive sharing](https://rominirani.com/docker-on-windows-mounting-host-directories-d96f3f056a2c#.w4v0e42tn).

4. Download a docker image by entering the following command in a terminal (PowerShell in Windows).

   ```shell
   docker pull shhongoist/a310_cns_2018
   ```

5. Download [start.sh](https://raw.githubusercontent.com/shhong/a310_cns_2017/master/docker_instruction_scripts/start.sh) (or [start.ps1](https://raw.githubusercontent.com/shhong/a310_cns_2017/master/docker_instruction_scripts/start.ps1) in Windows) and run it by

   ~~~shell
   ./start
   ~~~
   This starts a virtual linux environment that will give you a shell prompt as 

   ```
   root@4a946beb0dca:~/Documents#
   ```

   as you are in a directory `/root/Documents`. If drive sharing is correctly configured, this should be also your local directory.

6. It also starts a VNC server, which will give you access to the graphical user interface. Open [http://localhost:6901/vnc_auto.html?password=vncpassword]() for the virtual desktop.

7. Enter

   ~~~shell
   nrngui -python
   ~~~


   and see if it opens a window in the virtual desktop.

8. A [Jupyter notebook](http://jupyter.org) will also automatically start. Find the lines like

   ```bash
   Copy/paste this URL into your browser when you connect for the first time,
   to login with a token:
       http://0.0.0.0:8888/?token=127e39a78e32ea3989e066c52f38a439d0ff17869c4ad9b8
   ```

   in starting messages, and open the page in a web browser.



By default, the directory that contains the start script is mounted at `/root/Documents`. If you want to change this, edit the start script and change ${PWD} to a local directory you want to use.

The size of the desktop is 1620x1296. If you want to change this, change `VNC_RESOLUTION=1620x1296` in the start script to whichever size you want.


