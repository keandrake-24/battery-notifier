install:
	cp -r ./batterynotifier /usr/bin
	cp battery-notifier /usr/bin 
	chmod +x /usr/bin/batterynotifier

install-local:
	cp -r ./batterynotifier ~/.local/bin
	cp battery-notifier ~/.local/bin
	chmod +x ~/.local/bin/battery-notifier

uninstall-local:
	rm -r ~/.local/bin/batterynotifier
	rm ~/.local/bin/battery-notifier

uninstall:

	rm -r /usr/bin/batterynotifier
	rm /usr/bin/battery-notifier