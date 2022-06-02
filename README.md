# mobileconfigs

Configuration files for iOS.

## Getting started

Create a Python virtual environment and install dependencies:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Create a `.env` file and fill it as follows:

```
VPN_AUTOCONNECT_PPP_AUTH_NAME=johndoe
VPN_AUTOCONNECT_PPP_AUTH_PASSWORD=mysecretpassword
VPN_AUTOCONNECT_PPP_REMOTE_ADDR=vpn.example.com
VPN_AUTOCONNECT_IPSEC_PSK=mysecretpsk
VPN_AUTOCONNECT_ONDEMAND_SAFE_WIFI_SSIDS[]=[]
#VPN_AUTOCONNECT_ONDEMAND_SAFE_WIFI_SSIDS[]=['Home Sweet Home']
```

Render the `vpn.mobileconfig` template in the `public` folder:

```
$ ./render_template.py templates/vpn.mobileconfig.j2 > public/vpn.mobileconfig
```

Serve the `public` folder via HTTP:

```
$ python3 -m http.server 8080 -d public
```

Go to the website on your iPhone and download the `vpn.mobileconfig` file to install the VPN profile.

## License

This project is licensed under the [MIT No Attribution License](https://opensource.org/licenses/MIT-0) (MIT-0).
