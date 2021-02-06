# mobileconfigs

Configuration files for iOS. Tested platforms are:

- iOS 13
- iOS 14

This is licensed under the [MIT license](https://opensource.org/licenses/mit-license.php); see
LICENSE in the source distribution for details.

# Managing the configuration files

[Docker](https://www.docker.com/) and [Python](https://www.python.org/) `3.6` or newer are required
to manage the configuration files.

Run the following commands to create a new Python virtual environment and install the required
packages inside:

```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

In the root folder, create a `.env` file and fill it with the following fields:

```
VPN_AUTOCONNECT_PPP_AUTH_NAME=john
VPN_AUTOCONNECT_PPP_AUTH_PASSWORD=password
VPN_AUTOCONNECT_PPP_REMOTE_ADDR=vpn.john.com
VPN_AUTOCONNECT_IPSEC_PSK=vpn-pre-shared-key
VPN_AUTOCONNECT_ONDEMAND_SAFE_WIFI_SSIDS[]=[]
#VPN_AUTOCONNECT_ONDEMAND_SAFE_WIFI_SSIDS[]=['Home-Sweet-Home']
```

Run the following command to render the VPN configuration template and save it in the `public`
directory:

```
$ ./scripts/jinja2 templates/vpn.mobileconfig.j2 > public/vpn.mobileconfig
```

Configuration files in the `public` directory are served through an HTTP server at
`http://localhost:8080` with the following command:

```
$ ./scripts/serve-configs
```
