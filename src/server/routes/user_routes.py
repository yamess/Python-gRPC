import grpc

from configs.env_vars import SessionLocal, ACCESS_TOKEN_EXPIRE_MINUTES
from db.crud import create_user, get_user, update_user, update_pwd, delete_user, authenticate, create_access_token
from protos.user_pb2 import (
    CreateUserRequest,
    CreateUserResponse,
    GetUserRequest,
    GetUserResponse,
    UpdateUserRequest,
    UpdateUserResponse,
    UpdatePasswordRequest,
    UpdatePasswordResponse,
    DeleteUserRequest,
    DeleteUserResponse,
    LoginRequest,
    LoginResponse,
)
from protos.user_pb2_grpc import UserServiceServicer
import db.user_schema as sc
import logging

logger = logging.getLogger(__name__)


class UserService(UserServiceServicer):
    def Login(self, request: LoginRequest, context) -> LoginResponse:
        try:
            auth_data = {"email": request.email, "password": request.password}
            user = authenticate(session=SessionLocal(), auth_data=auth_data)
            if user:
                data = {
                    "user_id": user.id,
                    "email": user.email,
                    "is_active": user.is_active,
                    "is_admin": user.is_admin,
                }
                access_token = create_access_token(
                    to_encode=data, expires_delta=int(ACCESS_TOKEN_EXPIRE_MINUTES)
                )
                return LoginResponse(access_token=access_token)
        except Exception as e:
            logger.error(e)
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Error while authenticating")

    def CreateUser(self, request: CreateUserRequest, context) -> CreateUserResponse:
        try:
            user = sc.CreateUserRequest(
                email=request.email,
                password=request.password,
                is_active=request.is_active,
                is_admin=request.is_admin,
            )
            response = create_user(session=SessionLocal(), user=user)
            response = CreateUserResponse(
                id=response.id,
                email=response.email,
                is_active=response.is_active,
                is_admin=response.is_admin,
                created_at=str(response.created_at),
            )

            return response
        except Exception as e:
            logger.error(e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Error while saving record")

    def GetUser(self, request: GetUserRequest, context) -> GetUserResponse:
        try:
            user = get_user(session=SessionLocal(), user_id=request.id)
            response = GetUserResponse(
                id=user.id,
                email=user.email,
                is_active=user.is_active,
                is_admin=user.is_admin,
                created_at=str(user.created_at),
            )
            return response
        except Exception as e:
            logger.error(e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Error while getting record")

    def UpdateUser(self, request: UpdateUserRequest, context) -> UpdateUserResponse:
        try:
            user = update_user(session=SessionLocal(), data=request)
            response = UpdateUserResponse(
                id=user.id,
                email=user.email,
                is_active=user.is_active,
                is_admin=user.is_admin,
                created_at=str(user.created_at),
                updated_at=str(user.updated_at),
            )
            return response
        except Exception as e:
            logger.error(e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Error while Updating record")

    def UpdatePassword(
        self, request: UpdatePasswordRequest, context
    ) -> UpdatePasswordResponse:
        try:
            update_pwd(SessionLocal(), request)
            response = UpdatePasswordResponse(message="Password updated with success")
            return response
        except Exception as e:
            logger.error(e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Error while updating password")

    def DeleteUser(self, request: DeleteUserRequest, context) -> DeleteUserResponse:
        try:
            delete_user(session=SessionLocal(), user_id=request.id)
            response = DeleteUserResponse(message="User deleted with success")
            return response
        except Exception as e:
            logger.error(e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Error while delete user")
