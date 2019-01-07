# Installing NEURON via docker

1. Install [Docker Community Edition](https://www.docker.com/community-edition).

2. Start Docker.

3. In Windows, also [turn on drive sharing](https://rominirani.com/docker-on-windows-mounting-host-directories-d96f3f056a2c#.w4v0e42tn).

4. Download a docker image by entering the following command in a terminal (PowerShell in Windows).

   ```shell
   docker pull shhongoist/a310_cns_2018
   ```

5. Download [start.sh](https://raw.githubusercontent.com/CNS-OIST/a310_cns_2018/master/docker/start.sh) (or [start.ps1](https://raw.githubusercontent.com/CNS-OIST/a310_cns_2018/master/docker/start.ps1) in Windows) and run it by

   ~~~shell
   ./start.sh  # or .\start.ps1 in Windows
   ~~~
   This starts a virtual linux environment that will give you a shell prompt as 

   ```
   root@4a946beb0dca:~/Documents#
   ```

   as you are in a directory `/root/Documents`. If drive sharing is correctly configured, this should be also your local directory <sup>[1](#myfootnote0). 

6. It also starts a VNC server, which will give you access to the graphical user interface. Open http://localhost:6901/vnc_auto.html?password=vncpassword for the virtual desktop.

7. Enter

   ~~~bash
   nrngui -python
   ~~~


   and see that it opens a window in the virtual desktop<sup>[2](#myfootnote1),[3](#myfootnote2)</sup>.

8. A [Jupyter](http://jupyter.org) notebook will also automatically start. Find the lines like

   ```text
   Copy/paste this URL into your browser when you connect for the first time,
   to login with a token:
       http://0.0.0.0:8888/?token=127e39a78e32ea3989e066c52f38a439d0ff17869c4ad9b8
   ```

   in starting messages, and open the page in a web browser<sup>[4](#myfootnote3)</sup>.




## Additional notes

<a name="myfootnote0">1</a>. `start.ps1` may not run in Windows due to a security setting. Please change this accordingly as http://tritoneco.com/2014/02/21/fix-for-powershell-script-not-digitally-signed/.

<a name="myfootnote1">2</a>. By default, the directory that contains the start script is mounted at `/root/Documents`. If you want to change this, edit the start script and change ${PWD} to a local directory you want to use.

<a name="myfootnote2">3</a>. The size of the desktop is 1620x1296. If you want to change this, change `VNC_RESOLUTION=1620x1296` in the start script to whichever size you want.

<a name="myfootnote3">4</a>. In some systems, 0.0.0.0 may not be accessible. In this case replace 0.0.0.0 by localhost.

