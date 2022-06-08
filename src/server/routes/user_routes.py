from protos.user_pb2 import CreateUserRequest, CreateUserResponse, GetUserRequest, GetUserResponse, UpdateUserRequest, \
    UpdateUserResponse, UpdatePasswordRequest, UpdatePasswordResponse, DeleteUserRequest, DeleteUserResponse
from protos.user_pb2_grpc import UserServiceServicer


class UserService(UserServiceServicer):
    def Login(self, request, context):
        pass

    def CreateUser(self, request: CreateUserRequest, context) -> CreateUserResponse:
        print("Got request " + str(request))
        user = {
            "Email": request.email
        }

        return CreateUserResponse(email=user["Email"])

    def GetUser(self, request: GetUserRequest, context) -> GetUserResponse:
        pass

    def UpdateUser(self, request: UpdateUserRequest, context) -> UpdateUserResponse:
        pass

    def UpdatePassword(self, request: UpdatePasswordRequest, context) -> UpdatePasswordResponse:
        pass

    def DeleteUser(self, request: DeleteUserRequest, context) -> DeleteUserResponse:
        pass
