# QR Code or NFC Tag as Trigger to Launch Self-Hosted Page with Home Appliance / Part Information

URL Format:
```
https://your-domain.tld/q?t=1&id={{identifier_for_an_appliance}}
```

Examples of `identifier_for_an_appliance` include: 

* espresso 
* oven
* range
* microwave
...

JSON is used to store configuration information. Edit docker-compose with a bind pointing to your `config.json` file, which follows the format: 

```
{
	"identifier_for_an_appliance" : {
		"instructions" : "Lorem ipsum",
		"troubleshooting" : "Lorem ipsum",
		"notes" : "lorem ipsum",
		"name" : "appliance name",
		"model" : "abc123",
		"serial" : "123456789876543",
		"manufacturer" : "Jura",
		"links" : [
			{
				"name" : "Manual",
				"URL" : "xyz.pdf",
				"resource" : "PDF"
			},
			{
				"name" : "Warranty",
				"URL" : "xyz.pdf",
				"resource" : "PDF"
			}
		],
		"consumables" : [
			{
				"name" : "Product/Consumable product name",
				"URL" : "www.purchaseurl.com",
				"resource" : "Vendor/manufacturer",
				"description" : "Description of how used/why.",
			}
		]
	}
}
```

Config file should be added to `/data` directory if using an unmodified `docker-compose` file. 