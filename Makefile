generate-server:
	python -m grpc_tools.protoc --proto_path=src/protofiles --python_out=src/server/protos --grpc_python_out=src/server/protos $(protofile)

generate-client:
	python -m grpc_tools.protoc --proto_path=src/protofiles --python_out=src/client/protos --grpc_python_out=src/client/protos $(protofile)

generate-grpc: generate-server generate-client

start-evans:
	evans -r repl -p $(port)