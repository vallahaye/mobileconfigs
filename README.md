# mobileconfigs

Configuration files for iOS. Tested platforms are:

* iOS 13.6.1

`docker` and `python >=3.6` are required to manage the configs.

## Getting started

### Install dependencies

Run the following command to install the required Python libraries:

```
$ pip install -r requirements.txt
```

### Generate VPN configurations using Jinja2

In the root folder, create a `.env` file and fill it with the following fields:

```
VPN_AUTOCONNECT_PPP_AUTH_NAME=john
VPN_AUTOCONNECT_PPP_AUTH_PASSWORD=password
VPN_AUTOCONNECT_PPP_REMOTE_ADDR=vpn.john.com
VPN_AUTOCONNECT_IPSEC_PSK=vpn-pre-shared-key
VPN_AUTOCONNECT_ONDEMAND_SAFE_WIFI_SSIDS[]=[]
#VPN_AUTOCONNECT_ONDEMAND_SAFE_WIFI_SSIDS[]=['Home-Sweet-Home']
```

Run the following command to render the template in the console:

```
$ ./scripts/jinja2 templates/vpn.mobileconfig.j2
```

### Serving configurations on the network

Configurations in the `public` folder are served through an HTTP server at
`http://localhost:8080` with the following command:

```
$ ./scripts/serve-configs
```

## License

© 2020 Valentin Lahaye

This project is licensed under the terms of the MIT [license](LICENSE).
