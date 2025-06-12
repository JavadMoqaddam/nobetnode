from app.utils.ban import ban_ip, unban_ip
from app.service.nobetnode_grpc import NobetServiceBase
from app.service.nobetnode_pb2 import Result

class NobetService(NobetServiceBase):
    async def BanUser(self, stream):
        request = await stream.recv_message()

        ban_ip(request.ip,request.banDuration)

        reply = Result(success=True, message=f"Ip {request.ip} banned for {request.banDuration} seconds!")
        await stream.send_message(reply)
    
    async def UnBanUser(self, stream):
        request = await stream.recv_message()

        unban_ip(request.ip,request.banDuration)

        reply = Result(success=True, message=f"Ip {request.ip} unbanned!")
        await stream.send_message(reply)