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
		"manufacturer" : "Appliance",
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

## **Example for Jura Eno Micro 90**

### `config.json`

```
{
	"jura" : {
		"instructions" : "To use, power on. Clear any errors (fill water tank, empty tray, or empty grounds) displayed when the display has a red back light. For a milk drink, fill milk reservoir to labeled volume and connect hose to nozzle extending from the left of the brew group head. On the left side of the rotary, from top to bottom: (1) latte, (2) cappuccino, (3) macchiato. On the right side, from top to bottom: (1) hot water, (2) espresso, (3) coffee.",
		"notes" : "To control strength or liquid volume, you can rotate the dial.",
		"name" : "Jura Espresso Machine",
		"model" : "Eno Micro 90",
		"manufacturer" : "Jura",
		"links" : [
			{
				"name" : "Manual",
				"URL" : "https://www.williams-sonoma.com/netstorage/pdf/Jura-ENA-Micro-90-Manual-99001.pdf",
				"resource" : "PDF"
			},
			{
				"name" : "Parts",
				"URL" : "https://www.jura-parts.com/Jura-ENA-Micro-90-Parts-s/298.htm",
				"resource" : "PDF"
			}
		],
		"consumables" : [

			{
				"name" : "Little Owl Coffee",
				"URL" : "https://www.littleowlcoffee.com",
				"resource" : "Little Owl",
				"description" : "Denver-based Coffee Company."
			},
			{
				"name" : "Cleaning Agent",
				"URL" : "https://www.amazon.com/Jura-Cappuccino-Automatic-Machines-Frothing/dp/B000OF8ZJO/ref=sxin_0_ac_d_pm?ac_md=2-0-VW5kZXIgJDQw-ac_d_pm&cv_ct_cx=jura+cleaning+solution&keywords=jura+cleaning+solution&pd_rd_i=B000OF8ZJO&pd_rd_r=1c298e23-25da-488e-a0fb-d096a97bf98c&pd_rd_w=guHCi&pd_rd_wg=XJFmE&pf_rd_p=516e6e17-ed95-417b-b7a4-ad2c7b9cbae3&pf_rd_r=AEER6D4VW6K6JJMGBHBM&psc=1&qid=1585763915&s=home-garden&sr=1-1-22d05c05-1231-4126-b7c4-3e7a9c0027d0",
				"resource" : "Amazon",
				"description" : "Milk system cleaning agent. Should be used before powering down the machine after making one or more milk drinks. Fill front milk reservoir with water to 'clean' line and add 1oz of cleaning agent. Press rotary when powering down to confirm M-CLEAN and to confirm that the agent is added. Follow the remaining instructions."
			},
			{
                "name" : "Cleaning Tablets",
                "URL" : "https://www.amazon.com/Jura-64308-Cleaning-Tablets-Automatic/dp/B000BJSF6Q",
                "resource" : "Amazon",
				"description" : "Used when deep cleaning the machine. Tablet is added to the powder bypass doser when instructed."
            },
			{
				"name" : "Filter",
				"URL" : "https://www.amazon.com/Jura-Claris-Water-Filter-Pack/dp/B00E9V60FA/ref=sr_1_fkmr1_2?keywords=jura+evo+micro+90+filter&qid=1585763952&s=home-garden&sr=1-2-fkmr1",
				"resource" : "Amazon",
				"description" : "Water filter is in the rear of the machine, within the water reservoir."
			}
		]
	}
}
```

### **URL**

```
http://your-internal-ip:1987/q?t=1&id=jura
```

Encode the URL in a QR code (having an example IP address of `192.168.1.2`): ![example_qr](https://user-images.githubusercontent.com/6710151/78457895-d3c90900-766a-11ea-9d02-90dfcf37fe04.png)

### ** Results **

Now, whenever this QR code is scanned, a browser is launched with this information: 

![IMG_0702](https://user-images.githubusercontent.com/6710151/78458005-9e70eb00-766b-11ea-8a94-da76d01b3aa8.PNG)
