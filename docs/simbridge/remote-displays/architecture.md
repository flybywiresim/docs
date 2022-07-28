## Remote Display Architecture

The Simbridge uses a web application running in the browser to send and receive data via the Web Socket protocol from the displays in-sim.

To open the web application the browser will connect to the Simbridge's webserver via http protocol (default port 8380) and download and run the Remote Display Web Interface application (HTML/CSS/JavaScript).

The Remote Display Interface application will open a data connection to Simbridge via Web Socket protocol (default port 8380) and receive data (screen content) and send data (user input like button pushes) from and to the in-sim display.

For this to work the browser must be able to reach Simbridge via TCP port, 8380 (these defaults can be changed) which means users may need to reconfigure their network and firewall settings accordingly (see [configuration](../configuration.md#server-settings)).

!!! info Note
    Manual configuration is not usually required.
