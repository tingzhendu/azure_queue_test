# Azure messages and events
azure queue test code

let's see what the difference are between:
service:
1. Azure Service Bus (Message service)
2. Azure Storage Queue (Message service)
3. Azure Event Hub (Kafa like big data event driven)
4. Azure Event Grid (Reactive programming, very serveless) Interestingly, this contains Azure Blob Storage event but doesn't have Azure Table Storage Event. [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)
 provided this functoinality, people usually use it for record update(Push notification for price change or status update).


There's a documentation compare between Storage queues and Service Bus queues:
https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-azure-and-service-bus-queues-compared-contrasted



## How to run?
1. Use WSL under windows: 
    follow this awesome doc! https://docs.microsoft.com/en-us/windows/wsl/install-win10

2. If you haven't use windows terminal, You definitely should try it! It's awesome!
    https://github.com/microsoft/terminal

3. Install python3 and pip3 in your ubuntu subsystem, and clone this repo.

4. Since I'm lazy to create docker container, strongly recommand to use virtualenv to run the notebook. (Pip install virtualenv)

5. source bin/active, then pip install requirements.txt :)


6. type "jupyter notebook" 

You are good to go


