import grpc
from p4.v1 import p4runtime_pb2_grpc, p4runtime_pb2
from google.protobuf import wrappers_pb2

# Establish connection to the P4 switch via gRPC
channel = grpc.insecure_channel('0.0.0.0:9559')
stub = p4runtime_pb2_grpc.P4RuntimeStub(channel)

# Define the table entry to insert
entry = p4runtime_pb2.TableEntry()
entry.table_id = 1  # Set the correct table ID here
# Define match fields and actions for the entry
# (you'll need to convert your InsertRequest to this format)

# Insert the entry into the table
request = p4runtime_pb2.WriteRequest()
request.device_id = 0
#election_id = wrappers_pb2.UInt128(low=0, high=1)  # Create a Uint128 object
#request.election_id = election_id  # Assign it to election_id field
update = p4runtime_pb2.Update(
    type=p4runtime_pb2.Update.INSERT,  # Use 'type' instead of 'operation'
    entity=p4runtime_pb2.Entity(table_entry=entry)
)
request.updates.append(update)

# Send the request
stub.Write(request)
