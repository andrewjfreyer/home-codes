# QR Code / NFC Tag as Trigger to Launch Self-Hosted Page with aggregated Home Appliance / Part Information

## **TL;DR**

This is a quick containerized Flask project that consumes a JSON configuration file and serves, in response to a simple GET request, a Jinja template with that information. Intended use case is to encode a URL in a QR code printed on a label attached to a home appliance. 

## **How to Install**

1. Git clone: `git clone git://github.com/andrewjfreyer/home-codes.git`

2. Create `config.json` (see below) and store in root directory. 

3. `docker-compose up`

4. Access service (preferably locally) as described below

## **URL Format**

```
http://your-internal-ip:1987/q?t=1&id={{identifier_for_an_appliance}}
```

*Note: the `t` argument is reserved for future use cases with different types. At present, the type should always be 1.*

Examples of `identifier_for_an_appliance` include: 

* espresso 
* oven
* range
* microwave
...

The shorter the code, the less information must be encoded in a QR code comprising the URL. 

## **`config.json` File Format**

JSON is used to store configuration information. Edit docker-compose with a bind pointing to your `config.json` file, which follows the format: 

```
{
	"identifier_for_an_appliance" : {
		"instructions" : "To use this appliance... ",
		"troubleshooting" : "This machine is a bit finicky, try this...",
		"notes" : "This appliance has difficulty operating in cold temperatures...",
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