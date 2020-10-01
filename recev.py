import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore



# The code is orginal from tutorial
    
async def on_event(partition_context, event):
    # Print the event data.
    print("--Received the event: \"{}\" from the partition with ID: \"{}\"".format(event.body_as_str(encoding='UTF-8'), partition_context.partition_id))

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)

async def main():
    # Create an Azure blob checkpoint store to store the checkpoints.
    print('---in main')
    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string(conn_str="Endpoint=sb://tduevent.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=8DYYY3fCg+2CzhebahMUiWCUMnwP8Ekmb/15c8761zo=", 
                                                           consumer_group="$Default",  
                                                           eventhub_name="myeventhub")
    print('---done client')
    async with client:
        # Call the receive method. Read from the beginning of the partition (starting_position: "-1")
        print('--in client')
        await client.receive(on_event=on_event,  starting_position="-1")

loop = asyncio.get_event_loop()
# Run the main method.   
loop.run_until_complete(main())